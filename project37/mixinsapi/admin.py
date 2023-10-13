from django.contrib import admin

from mixinsapi.models import Employee, EmployeeDept

# Register your models here.
admin.site.register(EmployeeDept)
admin.site.register(Employee)