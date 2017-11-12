from django.db import models

from cars.models import Car
from users.models import CustomUser


class Driver(models.Model):
    full_name = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    schedule = models.TextField()
    pesel = models.TextField(max_length=11)
    profile_photo = models.ImageField()
    permissions_level = models.IntegerField()
    phone_number = models.TextField(max_length=15)
    user = models.OneToOneField(CustomUser, null= True)
    car = models.OneToOneField(Car, null= True)
