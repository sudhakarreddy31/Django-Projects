from urllib import request
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
from ormsapp.models import Employee

# Create your views here.


def employee_view(request):
    employees = Employee.objects.all()
    # employees = Employee.objects.filter (emp_salary__gte=50000)#filter function using employee salary greater than 50000
    # employees = Employee.objects.filter (emp_salary__te=50000)#filter function using employee salary lesst than 50000
    # employees = Employee.objects.get(emp_number__exact=17118)#extact to get employee_number id
    # employees = Employee.objects.get(emp_name__exact='SudhakarReddy')#Exactname
    # employees = Employee.objects.get(emp_name__icontains='SudhakarReddy')#Exactname
    # employees = Employee.objects.filter(emp_name__icontains='SudhakarReddy')#Exactname
    # employees = Employee.objects.filter(emp_name__iendswith='a')#endswith
    # employees = Employee.objects.filter(emp_name__startswith='a')#endswith
    # employees = Employee.objects.filter(emp_name__istartswith='S')#endswith
    # employees = Employee.objects.filter(emp_salary__range=(30000,80000))#endswith
    # employees= Employee.objects.filter(Q(emp_name__startswith='S') | Q(emp_salary__lt=50000))
    # employees = Employee.objects.filter (emp_number__in=[17118,6974,8631])#filter function using employee salary greater than 50000
    # employees= Employee.objects.filter(emp_name__startswith='J',emp_salary__lt=15000)
    # employees= Employee.objects.filter(emp_name__startswith='S') &Employee.objects.filter(emp_salary__lt=70000)
    # employees= Employee.objects.filter(Q(emp_name__startswith='a') & Q(emp_salary__lt=60000))
    return render(request,'ormsapp/employees.html',{'employees':employees})





def display_view(request):
    avg1=Employee.objects.all().aggregate(Avg('emp_salary'))
    max=Employee.objects.all().aggregate(Max('emp_salary'))
    min=Employee.objects.all().aggregate(Min('emp_salary'))
    sum=Employee.objects.all().aggregate(Sum('emp_salary'))
    count=Employee.objects.all().aggregate(Count('emp_salary'))

    my_dict={'avg':avg1,'max':max,'min':min,'sum':sum,'count':count}
    return render(request,'ormsapp/aggregate.html',my_dict)