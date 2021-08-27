from django.db import models

# Create your models here.
class Flats(models.Model):
    Bno=models.CharField(max_length=50)
    Oname=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)
    Adress=models.CharField(max_length=50)
    Adahar=models.CharField(max_length=50)
    Emailid=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

