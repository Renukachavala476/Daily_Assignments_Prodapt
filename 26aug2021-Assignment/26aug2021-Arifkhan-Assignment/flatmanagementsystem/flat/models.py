from django.db import models
class Flat(models.Model):
    bno=models.IntegerField()
    ownername=models.CharField(max_length=50)
    address=models.CharField(max_length=25)
    mobileno=models.BigIntegerField()
    addharno=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

