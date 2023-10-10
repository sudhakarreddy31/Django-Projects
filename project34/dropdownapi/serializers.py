from rest_framework import serializers
from dropdownapi.models import Country,City,Person



class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"



class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"




























