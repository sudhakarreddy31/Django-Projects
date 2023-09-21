
from cairo import STATUS_INVALID_CLUSTERS
from django.http import JsonResponse
from django.shortcuts import render 
from apiapp.models import Drink
from apiapp.serializers import Drinkserializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def drink_lists(request):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = Drinkserializer(drinks,many=True)
        return JsonResponse({'drinks':serializer.data})

    
    if request.method == 'POST':
        serializer = Drinkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def drink_details(request,id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Drinkserializer(drink)
        return Response(serializer.data)
    else:
        if request.method == 'PUT':
            serializer = Drinkserializer(drink,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        

        elif request.method == 'DELETE':
            drink.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    



















































