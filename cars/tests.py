from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from .models import Car


class CarTest(TestCase):

    def create_car(self, brand='Mazda', model='mx-5', production_year=1999, engine_volume=2.8,
                   body_type='sedan', need_repair='Igła, niemiec płakał jak sprzedawał',
                   insurance_number='LOLXD12345', is_available=True ):
        return Car.objects.create(
            brand=brand,
            model=model,
            production_year=production_year,
            engine_volume=engine_volume,
            body_type=body_type,
            need_repair=need_repair,
            insurance_number=insurance_number,
            is_available=is_available,
        )

    def test_read(self):
        w = self.create_car()
        d = Car.objects.get(id=w.id)
        self.assertEqual(d, w)

    def test_car_creation(self):
        w = self.create_car()
        self.assertTrue(isinstance(w, Car))
        self.assertEqual(w.brand, 'Mazda')
        self.assertEqual(w.model, 'mx-5')
        self.assertEqual(w.production_year, 1999)
        self.assertEqual(w.engine_volume, 2.8)
        self.assertEqual(w.body_type, 'sedan')
        self.assertEqual(w.insurance_number, 'LOLXD12345' )

    def test_car_update(self):
        c1 = self.create_car()

        fields = ['brand', 'model', 'production_year', 'insurance_number']

        c1.brand = 'Czołg'
        c1.model = 'Rudy'
        c1.production_year = 1939
        # c1.engine_volume = 256.800
        # problem z floatem przy assercie
        c1.insurance_number = 'BRAKCZOŁGISĄYOLO'

        c2 = Car.objects.get(id=c1.id)

        for i in fields:
            self.assertNotEqual(str(c1.__getattribute__(i)), str(c2.__getattribute__(i)))

        c1.save()
        c3 = Car.objects.get(id=c1.id)

        for i in fields:
            self.assertEqual(str(c1.__getattribute__(i)), str(c3.__getattribute__(i)))

    def test_delete(self):
        c1 = self.create_car()
        id = c1.id
        c1.delete()

        error_occured = False
        try:
            c2 = Car.objects.get(id=id)
        except ObjectDoesNotExist:
            error_occured = True

        self.assertTrue(error_occured)
