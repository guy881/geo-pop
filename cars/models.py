from django.db import models
# TODO from drivers.models import Driver


class Car(models.Model):
    car_id = models.IntegerField()
    is_available = models.BooleanField()
    state = models.TextField(max_length=50)
    coordinates = models.TextField(max_length=100)
    velocity = models.IntegerField()
    # TODO driver = models.OneToOneField(Driver)
