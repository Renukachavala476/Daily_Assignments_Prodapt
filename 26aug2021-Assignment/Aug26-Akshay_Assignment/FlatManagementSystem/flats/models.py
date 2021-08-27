from django.db import models

class Flats(models.Model):
    buildingno = models.IntegerField()
    ownername = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobno = models.BigIntegerField()
    aadharno = models.BigIntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)




