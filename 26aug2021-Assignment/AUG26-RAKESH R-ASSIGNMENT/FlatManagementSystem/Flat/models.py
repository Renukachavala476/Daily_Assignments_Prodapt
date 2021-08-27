from django.db import models

# Create your models here.
class Flat(models.Model):
   
    flat_no=models.CharField(max_length=100)
    building_no=models.CharField(max_length=150)
    owner_name=models.CharField(max_length=150)
    mobile_no=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    aadhar_no=models.CharField(max_length=150)
    email_id=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
