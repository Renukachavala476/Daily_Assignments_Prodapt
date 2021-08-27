from django.db import models

# Create your models here.
class Flat(models.Model):
    buildnum=models.CharField(max_length=50)
    oname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile=models.BigIntegerField(default=0)
    adhar=models.BigIntegerField(default=0)
    email=models.CharField(max_length=50)
    

