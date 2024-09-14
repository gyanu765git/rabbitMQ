from rest_framework import serializers
from .models import CollectData


# Write your serializers here

class CollectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectData
        fields = ["record",]