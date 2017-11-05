from django.db import models

from cars.models import Car
from users.models import CustomUser


class Driver(models.Model):
    driver_id = models.IntegerField()
    full_name = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    schedule = models.TextField()
    pesel = models.TextField(max_length=11)
    photo = models.ImageField()
    permissions_level = models.IntegerField()
    phone_number = models.TextField(max_length=15)
    user = models.OneToOneField(CustomUser)
    car = models.OneToOneField(Car)
