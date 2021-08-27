from django.db.models import fields
from rest_framework import serializers
from flats.models import Flat

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ('id','building_no','owner_name','address','mobile_no','aadhar_no','email','password')