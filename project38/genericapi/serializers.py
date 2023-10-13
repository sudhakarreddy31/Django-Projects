from rest_framework import serializers 
from .models import Employee,EmployeeDept

class EmployeeDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDept
        fields = "__all__"
        # depth=1

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        # depth=1