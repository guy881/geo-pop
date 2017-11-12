from django.test import TestCase
from .models import Driver
from django.core.exceptions import ObjectDoesNotExist


class DriverTest(TestCase):

    def create_driver(self, full_name="Test", gender="yes", pesel="132456789", permissions_level=1, phone_number=2):
        return Driver.objects.create(
            full_name=full_name,
            gender=gender,
            pesel=pesel,
            permissions_level=permissions_level,
            phone_number=phone_number
        )

    def test_read(self):
        w = self.create_driver()
        d = Driver.objects.get(id=w.id)
        self.assertEqual(d, w)

    def test_driver_creation(self):
        w = self.create_driver()
        self.assertTrue(isinstance(w, Driver))
        self.assertEqual(w.gender, 'yes')
        self.assertEqual(w.phone_number, 2)
        self.assertEqual(w.permissions_level, 1)

    def test_driver_update(self):
        d1 = self.create_driver()

        fields = ['full_name', 'gender', 'pesel', 'permissions_level', 'phone_number']

        d1.phone_number = 33
        d1.gender = 'Apache'
        d1.pesel = '6546546'
        d1.full_name = "grzesiek jestem"
        d1.permissions_level = 2

        d2 = Driver.objects.get(id=d1.id)

        for i in fields:
            self.assertNotEqual(str(d1.__getattribute__(i)), str(d2.__getattribute__(i)))

        d1.save()
        d3 = Driver.objects.get(id=d1.id)

        for i in fields:
            self.assertEqual(str(d1.__getattribute__(i)), str(d3.__getattribute__(i)))

    def test_delete(self):
        d1 = self.create_driver()
        id = d1.id
        d1.delete()

        error_occured = False
        try:
            d2 = Driver.objects.get(id=id)
        except ObjectDoesNotExist:
            error_occured = True

        self.assertTrue(error_occured)
