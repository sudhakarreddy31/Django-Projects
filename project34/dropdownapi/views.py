from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from dropdownapi.models import Country,City,Person
from dropdownapi.serializers import CountrySerializer,CitySerializer,PersonSerializer


# Create your views here.
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityListCreateView(generics.ListCreateAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        country_id = self.kwargs.get('country_id')
        return City.objects.filter(country_id=country_id)

    def list(self, request, *args, **kwargs):
        country_id = self.kwargs.get('country_id')
        queryset = self.get_queryset().filter(country_id=country_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


































