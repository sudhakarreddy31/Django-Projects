from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from mixinsapi.models import Employee,EmployeeDept
from mixinsapi.serializers import EmployeeDeptSerializer,EmployeeSerializer

# Create your views here.

class ListEmployeeMixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    


class EmployeeDetailMixins(mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    # def post(self,request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    

    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    




class EmployeeCreateMixins(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    













