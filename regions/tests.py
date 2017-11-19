from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from .models import Region, GeoLocalization


class RegionTest(TestCase):
    def create_region(self, is_updated=True,
                      last_updated=datetime(2009, 1, 6, 15, 8, 24, 78915)):
        loc1 = GeoLocalization.objects.create(latitude=35.21, longitude=64.145)
        loc2 = GeoLocalization.objects.create(latitude=37.65, longitude=68.145)
        return Region.objects.create(
            is_updated=is_updated,
            last_updated=last_updated,
            north_west=loc1,
            south_east=loc2,
        )

    def test_read(self):
        w = self.create_region()
        d = Region.objects.get(id=w.id)
        self.assertEqual(d, w)

    def test_region_creation(self):
        w = self.create_region()
        self.assertTrue(isinstance(w, Region))
        self.assertEqual(w.is_updated, True)
        # self.assertEqual(w.last_updated, datetime(2009, 1, 6, 15, 8, 24, 78915))

    def test_region_upis_updated(self):
        c1 = self.create_region()

        fields = ['is_updated']

        c1.is_updated = False
        # c1.last_updated = datetime(2009, 1, 6, 15, 8, 24, 78915)
        # problem z datą i timezoneami

        c2 = Region.objects.get(id=c1.id)

        for i in fields:
            self.assertNotEqual(str(c1.__getattribute__(i)), str(c2.__getattribute__(i)))

        c1.save()
        c3 = Region.objects.get(id=c1.id)

        for i in fields:
            self.assertEqual(str(c1.__getattribute__(i)), str(c3.__getattribute__(i)))

    def test_delete(self):
        c1 = self.create_region()
        id = c1.id
        c1.delete()

        error_occured = False
        try:
            c2 = Region.objects.get(id=id)
        except ObjectDoesNotExist:
            error_occured = True

        self.assertTrue(error_occured)
