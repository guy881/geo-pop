from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from regions.models import GeoLocalization
from .models import Obstacle


class UpdateTest(TestCase):
    def create_obstacle(self, date=datetime(2009, 1, 6, 15, 8, 24, 78915),
                        status='1', type='I02', result='S07'):

        loc1 = GeoLocalization.objects.create(latitude=35.21, longitude=64.145)
        return Obstacle.objects.create(
            date=date,
            localization=loc1,
            status=status,
            type=type,
            result=result,
        )

    def test_read(self):
        w = self.create_obstacle()
        d = Obstacle.objects.get(id=w.id)
        self.assertEqual(d, w)

    def test_obstacle_creation(self):
        w = self.create_obstacle()
        self.assertTrue(isinstance(w, Obstacle))
        self.assertEqual(w.date, datetime(2009, 1, 6, 15, 8, 24, 78915))
        self.assertEqual(w.status, '1')
        self.assertEqual(w.type, 'I02')
        self.assertEqual(w.result, 'S07')

    def test_obstacle_update(self):
        c1 = self.create_obstacle()

        fields = ['status', 'type', 'result']

        c1.date = datetime(2009, 1, 6, 15, 8, 24, 78915)
        # problem z datą i timezonami
        c1.status = '3'
        c1.type = 'I09'
        c1.result = 'J04'

        c2 = Obstacle.objects.get(id=c1.id)

        for i in fields:
            self.assertNotEqual(str(c1.__getattribute__(i)), str(c2.__getattribute__(i)))

        c1.save()
        c3 = Obstacle.objects.get(id=c1.id)

        for i in fields:
            self.assertEqual(str(c1.__getattribute__(i)), str(c3.__getattribute__(i)))

    def test_delete(self):
        c1 = self.create_obstacle()
        id = c1.id
        c1.delete()

        error_occured = False
        try:
            c2 = Obstacle.objects.get(id=id)
        except ObjectDoesNotExist:
            error_occured = True

        self.assertTrue(error_occured)
