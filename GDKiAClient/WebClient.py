import urllib3
import lxml
import bs4
from datetime import datetime
import re

# from updates.models import Obstacle
from decimal import Decimal


# from regions.models import GeoLocalization



class WebClient:
    requestUrl = 'http://www.gddkia.gov.pl/dane/zima_html/utrdane.xml'
    http = urllib3.PoolManager()

    def get_obstacles_data(self):
        data = self.http.request('GET', self.requestUrl).data
        return bs4.BeautifulSoup(data, 'xml')


class ObstaclesDataModel:
    def __init__(self, soup):
        self.soup = soup

    def parse_date(self, date):  # 2017-10-25T16:00:00+0200
        date_clear_pattern = '\+\d+'
        clear_date = re.sub(date_clear_pattern, '', date)
        return datetime.strptime(clear_date, '%Y-%m-%dT%X')

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

    def get_collection_of_obstacles(self):
        result = []
        i = 0

        for obstacle in self.soup.utrudnienia:
            if obstacle.typ.string == 'U':  # I type does not have this info
                print(self.determine_status(obstacle))
                print(self.determine_result(obstacle))
            #not enough info in GDKiA feed to determine "choice" like "Pielgrzymka", "Rajd" or anything
            #we should use ('I04', 'Inne'),

            # geoloc = GeoLocalization(latitude=Decimal(obstacle.geo_lat.string),
            #                        longitude=Decimal(obstacle.geo_long.string))
            
            # obstacle_from_db = Obstacle(date=self.parse_date(obstacle.data_likwidacji.string),
            # localization=geoloc,
            # type=obstacle.rodzaj.poz.string)

            if i > 20:
                break
            i = i + 1


webClient = WebClient()
data = webClient.get_obstacles_data()
model = ObstaclesDataModel(data)

model.get_collection_of_obstacles()
