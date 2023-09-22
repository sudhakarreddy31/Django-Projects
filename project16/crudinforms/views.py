from django.shortcuts import get_object_or_404, redirect, render

from crudinforms.models import Employee
from crudinforms.forms import EmployeeForm

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'crudinforms/employees_list.html',{'employees':employees})


def employee_create_view(request):
    form=EmployeeForm()

    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employee_lists')


    return render(request,'crudinforms/employee_form.html',{'form':form})


def employee_update_view(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employee_lists')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'crudinforms/employee_update.html', {'form': form})


def employee_delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/employee_lists')





















































