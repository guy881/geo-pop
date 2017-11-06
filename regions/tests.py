from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Regions
from .models import GeoLocalization


class RegionTests(TestCase):

def create_region(self, date, x1, y1, x2, y2):
		a = GeoLocalization.objects.create(
            latitude=x1
			longitude=y1
        )
		b = GeoLocalization.objects.create(
            latitude=x2
			longitude=y2
        )
        return Region.objects.create(
            is_updated=True
            last_updated=date,
            north_west=a,
            south_east=b
        )

    def openedRegionSite(self):
		obsz1 = self.create_region(12/12/2015, 53.00, 15.00, 52.00, 17.00)
		obsz2 = self.create_region(19/03/2016, 53.00, 17.00, 52.00, 19.00)
		map = [obsz1, obsz2]
		Regions.objects.create()
        response = client.get('/regions')
		
		self.assertEqual(response.status_code, 200)
        self.assertContains(response, map)