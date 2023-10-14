from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from tokenapi.models import Bike
from tokenapi.serializers import BikeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
# Create your views here.
# @permission_classes([IsAuthenticated])
class BikeListView(APIView):

    #  Below Step for login for SessionAuthentication BasicAuthentication
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bikes = Bike.objects.all()
        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# @permission_classes([IsAuthenticated])
class BikeDetailView(APIView):




    def get(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        serializer = BikeSerializer(bike)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BikeCreateView(APIView):
    def post(self, request):
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BikeUpdateView(APIView):
    def put(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        serializer = BikeSerializer(bike, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BikeDeleteView(APIView):
    def delete(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        bike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




















