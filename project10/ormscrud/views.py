from django.shortcuts import render

from ormscrud.models import Employee

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'ormscrud/employee_list.html',{'employees':employees})

