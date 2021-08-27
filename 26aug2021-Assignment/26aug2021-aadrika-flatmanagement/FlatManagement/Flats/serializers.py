from rest_framework import serializers
from Flats.models import Flat

class FlatsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=('id','buildnum','oname','address','mobile','adhar','email')