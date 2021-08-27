from rest_framework import serializers
from flats.models import Flats

class FlatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flats
        fields = ('id','buildingno','ownername','address','mobno','aadharno','email','password')