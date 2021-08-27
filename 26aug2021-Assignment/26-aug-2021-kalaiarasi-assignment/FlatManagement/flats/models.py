from django.db import models

# Create your models here.
class Flat(models.Model):
    buildingno=models.IntegerField()
    ownername=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    Mobnum=models.BigIntegerField()
    adhaarno=models.BigIntegerField()
    emailid=models.EmailField(max_length=50)
    password=models.IntegerField()
    