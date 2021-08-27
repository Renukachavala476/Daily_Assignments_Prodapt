from rest_framework import serializers
from flat.models import Flats

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flats
        fields=('id','buildnum','name','address','mobile','aadhar','email')
