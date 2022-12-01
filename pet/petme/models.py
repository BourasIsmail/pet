from django.db import models

class User(models.Model):
    full_name = models.TextField(null=True, blank=True)
    email = models.EmailField(primary_key=True, blank=True)
    pwd = models.TextField(null=True, blank=True)
    Role = models.TextField(null=True , blank=True)


class Pet(models.Model):
    id = models.TextField(primary_key=True, blank=True)
    name = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True , blank=True)
    race = models.TextField(null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    EtatVaccin = models.BooleanField(null=True , blank=True)
    EtatAdopt = models.BooleanField(null=True , blank=True)
    EtatDressage = models.BooleanField(null=True , blank=True)
    Added = models.DateField(null=True , blank=True)
    EtatCastre = models.BooleanField(null=True, blank=True)


# Create your models here.
