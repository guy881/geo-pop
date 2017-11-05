from django.db import models


class Driver(models.Model):
    full_name = models.TextField(max_length=50)
    gender = models.TextField(max_length=50)
    # TODO: harmonogram
    pesel = models.TextField(max_length=11)
    # TODO: PHOTO
    image = models.ImageField(blank=True, null= True)
    permissions_level = models.IntegerField(default=0)  # TODO: do przegadania
    phone_number = models.TextField(max_length=15)

    def __str__(self):
        return self.full_name + ' ' + self.pesel
