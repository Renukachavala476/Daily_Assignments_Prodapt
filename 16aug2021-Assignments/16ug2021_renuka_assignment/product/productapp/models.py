from django.db import models
class Product(models.Model):
    pcode=models.IntegerField()
    pname=models.CharField(max_length=50,default='NO NAME',blank=True)
    pdes=models.CharField(max_length=50)
    price=models.IntegerField()
