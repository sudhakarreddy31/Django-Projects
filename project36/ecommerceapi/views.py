from django.shortcuts import render
from ecommerceapi.models import Product
from ecommerceapi.serializers import ProductSerializer,SampleSerializer
from .test import SampleComment
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])   # User Login perpose
def list_products(request):
    products = Product.objects.all()
    serializer_class_data = ProductSerializer(products,many=True)
    # context = {
    #     "serializer_class_data" : "serializer_class_data"
    # }

    return Response(serializer_class_data.data)

# Sample Serializer
@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def samplecomment(request):
    sample = SampleComment('Sudhakar@gmail.com','Hello SudhakarReddy')
    serializer_class_data = SampleSerializer(sample)

    return Response(serializer_class_data.data)


# class based Views

class ProductListView(APIView):
    def get(self,request):
        queryset = Product.objects.all()
        serializer_class_data = ProductSerializer(queryset,many=True)
        return Response(serializer_class_data.data)
    

    def post(self,request):
        serializer_class_data = ProductSerializer(data=request.data)
        if serializer_class_data.is_valid(raise_exception=True):
            product_saved = serializer_class_data.save()
            return Response({"Success":"Product '{}' Created Sucessfully".format(product_saved.name)})
        
        return Response(serializer_class_data.errors,status=status.HTTP_400_BAD_REQUEST)
            


class ProductDetailView(APIView):
    def get(self,request,pid):
        queryset = Product.objects.filter(product_id=pid)
        serializer_class_data = ProductSerializer(queryset,many=True)
        return Response(serializer_class_data.data)


    def put(self,request,pid):
        products=Product.objects.get(product_id=pid)
        serializer_class_data = ProductSerializer(data=request.data)
        if serializer_class_data.is_valid(raise_exception=True):
            product_saved = serializer_class_data.save()
            return Response({"Success":"Product '{}' Updated Sucessfully".format(product_saved.name)})
        
        return Response(serializer_class_data.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pid):
        products=Product.objects.filter(product_id=pid).delete()
        return Response(status=status.HTTP_200_OK)









































