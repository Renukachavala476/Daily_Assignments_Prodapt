from rest_framework import serializers
from flat.models import Flat
class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=("id","bno","ownername","address","mobileno","addharno","email","username","password")