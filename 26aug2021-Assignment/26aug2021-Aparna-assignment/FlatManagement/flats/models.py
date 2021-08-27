from django.db import models

# Create your models here.
class Flat(models.Model):
    building_no = models.CharField(max_length=10)
    owner_name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    aadhar_no = models.CharField(max_length=12)
    email = models.CharField(max_length=25)
    password =models.CharField(max_length=15)
    
