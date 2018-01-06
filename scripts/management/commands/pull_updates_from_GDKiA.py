import bs4
import urllib3
from django.core.management import BaseCommand

from regions.models import GeoLocalization, Region
from updates.models import Obstacle
import re
from datetime import datetime


class Command(BaseCommand):
    help = "Pobieranie aktualizacji z GDDKiA"

    def handle(self, *args, **options):
        webClient = WebClient()
        data = webClient.get_obstacles_data()
        mapper = Mapper()
        toBeInserted = []
        utrudnienia_mazowieckie = [x for x in data.utrudnienia if x.woj.string == "mazowieckie"]
        Obstacle.objects.all().delete()
        for count, obstacleFromGDKiA in enumerate(utrudnienia_mazowieckie):
            obstacle = mapper.map_soup_object_to_obstacle(obstacleFromGDKiA)
            if obstacle is not None:
                toBeInserted.append(obstacle)

        for count, obstacle in enumerate(toBeInserted):
            obstacle.localization.save()
            obstacle.localization_id = obstacle.localization.id
            obstacle.save()
        return str(toBeInserted.__len__())


def parse_date(date):  # 2017-10-25T16:00:00+0200
    date_clear_pattern = '\+\d+'
    clear_date = re.sub(date_clear_pattern, '', date)
    return datetime.strptime(clear_date, '%Y-%m-%dT%X')


class Mapper:
    def map_soup_object_to_obstacle(self, obstacle):
        if obstacle.typ.string == 'U':  # I type does not have this info
            '''
        print("___________________________________________")
        print("Opis: ", self.determine_description(obstacle))
        print("Współrzędne: ", self.determine_location(obstacle))
        print("Status:", self.determine_status(obstacle))
        print("Wynik:", self.determine_result(obstacle))
        start, stop = self.determine_datetime(obstacle)
        print(f"Czas zgłoszenia: {start} \nCzas likwidacji: {stop}")
        print("Ograniczenie predkosci", obstacle.ogr_predkosc.string)
        '''
            obstaclemodel = Obstacle()
            obstaclemodel.date = self.determine_datetime(obstacle)
            obstaclemodel.status = self.determine_status(obstacle)
            obstaclemodel.type = obstacle.rodzaj.poz.string
            obstaclemodel.result = self.determine_result(obstacle)
            geoloc = GeoLocalization()
            geoloc.latitude, geoloc.longitude = self.determine_location(obstacle)
            obstaclemodel.localization = geoloc

            # mark region containing that point as updated
            region = Region.objects.filter(
                north_west__latitude__gt=geoloc.latitude,
                north_west__longitude__lt=geoloc.longitude,
                south_east__latitude__lt=geoloc.latitude,
                south_east__longitude__gt=geoloc.longitude).first
            if region is not None:
                region.is_updated = True
                region.last_updated = datetime.now()
                region.updated_by = 'GDDKiA'
                region.save()

            return obstaclemodel
        return None

    def determine_location(self, obstacle):
        if obstacle.geo_lat != None and obstacle.geo_long:
            lat = float(obstacle.geo_lat.string)
            long = float(obstacle.geo_long.string)
            return lat, long

    def determine_datetime(self, obstacle):
        if obstacle.data_powstania and obstacle.data_likwidacji:
            start = parse_date(obstacle.data_powstania.string)
            stop = parse_date(obstacle.data_likwidacji.string)
            return stop

    def determine_description(self, obstacle):
        if obstacle.objazd:
            return obstacle.objazd.string

    def determine_status(self, obstacle):
        '''
        <ruch_wahadlowy>false</ruch_wahadlowy>
        <sygnalizacja_swietlna>false</sygnalizacja_swietlna>
        <awaria_mostu>false</awaria_mostu>
        <ruch_2_kierunkowy>false</ruch_2_kierunkowy>
        <droga_zamknieta>false</droga_zamknieta>
        '''
        if bool(obstacle.droga_zamknieta.string):
            return 8
        if bool(obstacle.sygnalizacja_swietlna.string) \
                or bool(obstacle.ruch_wahadlowy.string) \
                or bool(obstacle.awaria_mostu.string):
            return 3
        return 1

    def determine_result(self, obstacle):
        if bool(obstacle.droga_zamknieta.string):
            return 'S02'
        if bool(obstacle.ruch_wahadlowy.string):
            return 'S06'
        return 'S04'


class WebClient:
    requestUrl = 'http://www.gddkia.gov.pl/dane/zima_html/utrdane.xml'
    http = urllib3.PoolManager()

    def get_obstacles_data(self):
        data = self.http.request('GET', self.requestUrl).data
        # print(bs4.BeautifulSoup(data, 'xml').prettify())
        return bs4.BeautifulSoup(data, 'xml')
