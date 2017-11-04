from django.db import models
from drivers.models import Driver


class Car(models.Model):
    is_available = models.BooleanField()
    state = models.TextField(max_length=50)
    coordinates = models.TextField(max_length=100)
    velocity = models.IntegerField()
    driver = models.ForeignKey(Driver)