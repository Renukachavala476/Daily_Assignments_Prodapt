from django.db import models
class Seller(models.Model):
    sellerid=models.IntegerField()
    sellername=models.CharField(max_length=50,default='NO NAME',blank=True)
    address=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
