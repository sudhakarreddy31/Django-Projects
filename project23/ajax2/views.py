from django.http import JsonResponse
from django.shortcuts import render

from ajax2.models import Employee

# Create your views here.

def index(request):
    return render(request,'ajax2/index.html')

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        dept = request.POST['dept']
        location = request.POST['location']

        new_list=Employee(name=name,number=number,dept=dept,location=location)
        new_list.save()
        success = 'Profiles Created Successfullay for ' + name
        return JsonResponse({'success': success})
    

