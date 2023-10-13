from django.shortcuts import render
from genericapi.models import Employee
from genericapi.serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework import serializers
from rest_framework import viewsets
# from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.

# <-------------------Generic Views Started ------------->
# @permission_classes([IsAuthenticated])
class EmployeeGerericView(generics.ListAPIView):

    # Below Step for login for SessionAuthentication BasicAuthentication
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]


    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeGerericCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeGerericDetail(
                            generics.UpdateAPIView,
                            generics.DestroyAPIView
                            ):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



# <-------------------Generic Views Ended ------------->


# <-------------------Viewsets Ended ------------->


class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer














