from django.db import models

from cars.models import Car
from users.models import CustomUser


class Driver(models.Model):
    PERMISSIONS_CHOICES = (
        ('AM', 'Prawo jazdy kategori AM'),
        ('A', 'Prawo jazdy kategori A'),
        ('A1', 'Prawo jazdy kategori A1'),
        ('A2', 'Prawo jazdy kategori A2'),
        ('B', 'Prawo jazdy kategori B'),
        ('B+E', 'Prawo jazdy kategori B+E'),
        ('C', 'Prawo jazdy kategori C'),
        ('C+E', 'Prawo jazdy kategori C+E'),
        ('C1', 'Prawo jazdy kategori C1'),
        ('C1+E', 'Prawo jazdy kategori C+E'),
        ('D', 'Prawo jazdy kategori D'),
        ('D+E', 'Prawo jazdy kategori D+E'),
        ('D1', 'Prawo jazdy kategori D1'),
        ('D1+E', 'Prawo jazdy kategori D1+E'),
    )
    full_name = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    schedule = models.TextField()
    pesel = models.TextField(max_length=11)
    profile_photo = models.ImageField()
    permissions_level = models.CharField(max_length=50, choices=PERMISSIONS_CHOICES)
    phone_number = models.TextField(max_length=15)
    user = models.OneToOneField(CustomUser, null=True)
    car = models.OneToOneField(Car, null=True)
