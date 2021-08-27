from rest_framework import serializers
from Flat.models import Flat


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=('id','flat_no','building_no','owner_name','mobile_no','address','aadhar_no','email_id','password')