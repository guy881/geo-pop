from django.db import models


class GeoLocalization(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Region(models.Model):
    is_updated = models.BooleanField()
    last_updated = models.DateTimeField()
    # top left and bottom right corner of region
    north_west = models.ForeignKey(GeoLocalization, on_delete=models.CASCADE, parent_link=True,
                                   related_name='region_south_east')
    south_east = models.ForeignKey(GeoLocalization, on_delete=models.CASCADE, parent_link=True)
