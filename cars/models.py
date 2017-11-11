from django.db import models

from regions.models import GeoLocalization


class Car(models.Model):
    BODY_TYPE_CHOICES = (
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('kombi', 'Kombi'),
        ('suv', 'SUV'),
        ('truck', 'Truck'),
        ('van', 'Van')
    )

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    production_year = models.IntegerField()
    engine_volume = models.DecimalField(decimal_places=3, max_digits=8)
    body_type = models.CharField(max_length=10, choices=BODY_TYPE_CHOICES, default='sedan')
    need_repair = models.TextField(max_length=50, null=True, blank=True)
    insurance_number = models.CharField(max_length=50, null=True, blank=True)
    is_available = models.BooleanField()
    last_location = models.OneToOneField(GeoLocalization,null=True)
