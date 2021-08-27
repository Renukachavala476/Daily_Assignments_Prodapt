from django.db import models

# Create your models here.
class Flats(models.Model):
    buildnum=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile=models.BigIntegerField(default=0)
    aadhar=models.BigIntegerField(default=0)
    email=models.CharField(max_length=50)
