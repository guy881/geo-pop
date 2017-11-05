from django.db import models

# TODO from drivers.models import Driver
from drivers.models import Driver
from regions.models import GeoLocalization


class Car(models.Model):
    car_id = models.IntegerField()
    make = models.CharField()
    model = models.CharField()
    production_year = models.IntegerField()
    engine_volume = models.DecimalField()
    bodyType = (
        (1, 'Sedan')
        (2, 'Hatchback')
        (3, 'Kombi')
        (4, 'SUV')
        (5, 'Truck')
        (6, 'Van')
    )
    need_repair = models.TextField(max_length=50)
    insurance_number = models.CharField()
    is_available = models.BooleanField()
    last_location = models.OneToOneField(GeoLocalization)
    driver = models.ManyToManyField(Driver)
