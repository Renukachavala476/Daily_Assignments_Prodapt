from rest_framework import serializers
from flats.models import Flats

class FlatSerialize(serializers.ModelSerializer):
    class Meta:
        model=Flats
        fields=('id','Bno','Oname','Mobile','Adress','Adahar','Emailid','Password')