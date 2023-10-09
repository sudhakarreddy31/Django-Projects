from django.shortcuts import redirect, render
from apiapps.models import Task
from apiapps.serializers import TaskSerializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def task_lists(request):
    tasks = Task.objects.all()
    serializers = TaskSerializers(tasks,many=True)
    return Response(serializers.data)



@api_view(['GET'])
def task_detail(request,pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializers(task)
    return Response(serializers.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def task_update(request,pk):
    task = Task.objects.get(id=pk)
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return 200 OK

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def task_delete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')




