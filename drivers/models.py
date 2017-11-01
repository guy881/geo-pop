from django.db import models


class Driver(models.Model):
    full_name = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    # TODO: harmonogram
    pesel = models.TextField(max_length=11)
    # TODO: PHOTO
    permissions_level = models.IntegerField()  # TODO: do przegadania
    phone_number = models.TextField(max_length=15)

    def __str__(self):
        return self.full_name + ' ' + self.pesel
