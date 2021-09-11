from django.db import models

class Donors(models.Model):

    
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    bgroup = models.CharField(max_length=50)
    mobno = models.BigIntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
