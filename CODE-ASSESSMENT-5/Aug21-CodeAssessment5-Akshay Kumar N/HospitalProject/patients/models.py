from django.db import models

class Patients(models.Model):
    pcode = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    admitstatus = models.CharField(max_length=50)