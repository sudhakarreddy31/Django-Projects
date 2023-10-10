from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dependentapi.models import City, Student
from dependentapi.serializers import CitySerializer, StudentSerializer


# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CityByCountryAPIView(APIView):
    def get(self, request):
        country_id = request.GET.get('country')
        if country_id:
            cities = City.objects.filter(country_id=country_id)
            city_data = [{'id': city.pk, 'name': city.name} for city in cities]
            return JsonResponse(city_data, safe=False)
        else:
            return JsonResponse({'error': 'Invalid country ID'}, status=status.HTTP_400_BAD_REQUEST)

