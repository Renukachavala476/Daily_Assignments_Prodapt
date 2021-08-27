from rest_framework import serializers
from flats.models import Flat

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=('id','buildingno','ownername','address','Mobnum','adhaarno','emailid','password')

