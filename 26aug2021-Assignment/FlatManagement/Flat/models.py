from django.db import models
#building no,owner name,address,mobile no,aadhar number, email id, Password 
class FlatModel(models.Model):
    bno=models.IntegerField()
    ownername=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    aadhar=models.BigIntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)


    