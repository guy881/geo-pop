from django.db import models

# Create your models here.
from drivers.models import Driver


class GeoLocalization(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    class Meta:
        proxy = True



class Region(models.Model):
    is_updated = models.BooleanField()
    last_updated = models.DateTimeField()
    driver = models.OneToOneField(Driver)
    north_west = models.OneToOneField(GeoLocalization, on_delete=models.CASCADE, parent_link=True)
    north_east = models.OneToOneField(GeoLocalization, on_delete=models.CASCADE, parent_link=True)
    south_west = models.OneToOneField(GeoLocalization, on_delete=models.CASCADE, parent_link=True)
    north_east = models.OneToOneField(GeoLocalization, on_delete=models.CASCADE, parent_link=True)