from django.db import models
from rest_framework import serializers
from Flat.models import FlatModel

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlatModel
        fields=('id','bno','ownername','address','mobile','aadhar','email','password')