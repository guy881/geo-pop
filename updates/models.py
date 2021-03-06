from django.db import models

from drivers.models import Driver
from regions.models import GeoLocalization


class Obstacle(models.Model):
    date = models.DateField()
    localization = models.OneToOneField(GeoLocalization)
    STATUS_CHOICES = (
        ('1', 'Warunki jazdy bez utrudnień'),
        ('3', 'Utrudnione warunki jazdy'),
        ('8', 'Droga zamknięta')
    )
    TYPE_CHOICES = (
        ('I02', 'Blokada drogi'),
        ('I04', 'Inne'),
        ('I05', 'Rajd'),
        ('I06', 'Pielgrzymka'),
        ('I07', 'Zawody sportowe'),
        ('I08', 'Demonstracja'),
        ('I09', 'Uroczystość'),
        ('I10', 'Przejazd ważnej osobistości'),
        ('I11', 'Przejazd pojazdu nienormatywnego'),
        ('I12', 'Zwiększone natężenie ruchu'),
        ('I13', 'Protest'),
        ('K00', 'Katastrofa budowlana'),
        ('K01', 'Katastrofa ekologiczna'),
        ('K02', 'Pożar'),
        ('K03', 'Inne'),
        ('K04', 'Powódź'),
        ('S00', 'Brak informacji'),
        ('U27', 'Remont mostu'),
        ('U33', 'Roboty drogowe'),
        ('U42', 'Inne'),
        ('R00', 'Zderzenie się pojazdów w ruchu - czołowe'),
        ('R01', 'Zderzenie się pojazdów w ruchu - boczne'),
        ('R02', 'Zderzenie się pojazdów w ruchu - tylne'),
        ('R03', 'Najechanie pojazdu na pieszego'),
        ('R04', 'Najechanie pojazdu na pojazd unieruchomiony'),
        ('R05', 'Najechanie pojazdu na drzewo, słup'),
        ('R06', 'Najechanie pojazdu na zaporę kolejową'),
        ('R07', 'Najechanie pojazdu na urządzenie drogowe'),
        ('R08', 'Najechanie pojazdu na zwierzę'),
        ('R09', 'Wywrócenie się pojazdu'),
        ('R10', 'Inne'),
        ('R11', 'Zderzenie się pojazdów w ruchu'),
        ('R12', 'Wypadnięcie pojazdu z jezdni'),
        ('R13', 'Wjechanie pojazdu do rowu'),
        ('R14', 'Awaria pojazdu')
    )
    RESULT_CHOICES = (
        ('J00', 'Brak informacji'),
        ('J01', 'Wytyczony objazd'),
        ('J02', 'Przerwa w ruchu'),
        ('J03', 'Kierowanie ruchem przez policję'),
        ('J04', 'Inne'),
        ('J05', 'Zator drogowy'),
        ('S00', 'Brak informacji'),
        ('S02', 'Przerwa w ruchu'),
        ('S01', 'Wytyczony objazd'),
        ('S03', 'Kierowanie ruchem przez policję'),
        ('S04', 'Inne'),
        ('S05', 'Droga zablokowana'),
        ('S06', 'Ruch wahadłowy'),
        ('S07', 'Zablokowany pas ruchu'),
        ('S08', 'Zablokowana część pasa ruchu'),
        ('S09', 'Zablokowane pobocze')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    result = models.CharField(max_length=50, choices=RESULT_CHOICES)

    class Photo(models.Model):
        image = models.ImageField(null=True)
        location = models.ForeignKey(GeoLocalization)
        created_date = models.DateTimeField(null=True)
        send_date = models.DateTimeField()
        driver = models.ForeignKey(Driver)
