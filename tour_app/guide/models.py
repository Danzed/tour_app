from django.db import models

# Create your models here.
class Guide(models.Model):

    HOMBRE = 'hombre'
    MUJER = 'Mujer'

    GENDER_CHOICES = (
        (HOMBRE, 'Hombre'),
        (MUJER, 'Mujer'),
    )
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    whatsapp = models.BooleanField(default=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

class Place(models.Model):
    name_place = models.CharField(max_length = 100)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=11, decimal_places=7)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)


class Tour(models.Model):
    name_tour = models.CharField(max_length=100)

class Route(models.Model):
    tour = models.ForeignKey(Tour)
    place = models.ForeignKey(Place)
    