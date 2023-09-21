from django.shortcuts import redirect, render
from crudfbvapp.forms import EmployeeForm
from crudfbvapp.models import Employee

# Create your views here.



def read_view(request):
    employees = Employee.objects.all()
    return render(request, 'crudfbvapp/index.html',{'employees':employees})

def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/read/")
    return render(request, "crudfbvapp/create.html",{'form':form})


def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/read/")



def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method=='POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect("/read/")
    return render(request,'crudfbvapp/update.html',{'employee':employee})