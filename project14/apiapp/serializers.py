from apiapp.models import Drink
from rest_framework import serializers

class Drinkserializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

