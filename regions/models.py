from django.db import models

# Create your models here.

class GeoLocalization(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    class Meta:
        proxy = True



class Region(models.Model):
    north_west = models.OneToOneField(GeoLocalization, on_delete=models.CASCADE, parent_link=True)
    north_east = models.OneToOneField(GeoLocalization, on_delete=models.CASCADE, parent_link=True)
    south_west = models.OneToOneField(GeoLocalization, on_delete=models.CASCADE, parent_link=True)
    north_east = models.OneToOneField(GeoLocalization, on_delete=models.CASCADE, parent_link=True)