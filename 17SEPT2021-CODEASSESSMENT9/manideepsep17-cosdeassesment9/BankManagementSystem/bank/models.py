from django.db import models

# Create your models here.
class bank(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bankbalance=models.BigIntegerField()
    mobile=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.BigIntegerField()

class AdminRegisterModel(models.Model):
    ename=models.CharField(max_length=200)
    eemail=models.CharField(max_length=200)
    epassword=models.CharField(max_length=200)
    emobile=models.BigIntegerField()

class AdminloginModel(models.Model):
    eusername=models.CharField(max_length=200)
    epassword=models.CharField(max_length=200)
   