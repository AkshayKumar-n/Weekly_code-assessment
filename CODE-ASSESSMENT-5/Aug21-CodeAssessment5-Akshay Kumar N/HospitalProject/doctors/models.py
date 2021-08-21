from django.db import models

class Doctor(models.Model):
    dcode = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
