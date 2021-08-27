from django.db import models

# Create your models here.

class Flat(models.Model):
    BuildingNo=models.IntegerField()
    OwnerName=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    MobileNumber=models.CharField(max_length=50)
    AadhaarNumber=models.CharField(max_length=50)
    EmailId=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    #id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    

