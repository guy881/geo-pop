from django.db import models

from regions.models import GeoLocalization


class Car(models.Model):
    BODY_TYPE_CHOICES = (
        (1, 'Sedan'),
        (2, 'Hatchback'),
        (3, 'Kombi'),
        (4, 'SUV'),
        (5, 'Truck'),
        (6, 'Van')
    )
    
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    production_year = models.IntegerField()
    engine_volume = models.DecimalField(decimal_places=3, max_digits=8)
    body_type = models.CharField(max_length=10, choices=BODY_TYPE_CHOICES, default='1')
    need_repair = models.TextField(max_length=50)
    insurance_number = models.CharField(max_length=50)
    is_available = models.BooleanField()
    last_location = models.OneToOneField(GeoLocalization)
