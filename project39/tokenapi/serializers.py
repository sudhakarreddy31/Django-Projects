from rest_framework import serializers
from tokenapi.models import Bike

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = "__all__"
        # depth=1




















