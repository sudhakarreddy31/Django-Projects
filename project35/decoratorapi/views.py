from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from decoratorapi.models import Student
from decoratorapi.serializers import LoginSerializer, StudentSerializer
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    

    elif request.method == "POST":
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    

    elif request.method == 'PUT':
        data = request.data
        try:
            student = Student.objects.get(id=data['id'])
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=404)
        
        serializer = StudentSerializer(student, data=data)  # Corrected data format
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    
    elif request.method == 'PATCH':
        data = request.data
        try:
            student = Student.objects.get(id=data['id'])
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=404)
        
        serializer = StudentSerializer(student, data=data, partial=True)  # Corrected data format
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        data = request.data
        try:
            student = Student.objects.get(id=data['id'])
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=404)
        
        student.delete()  # Corrected method call
        return Response({'message': 'Successfully Deleted..!'}, status=204)


    