from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def register_form(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginform')
    else:
        form=UserCreationForm()
    return render(request,'registerform/register.html',{'form':form})


def login_form(request):
    return render(request,'registerform/login_form.html')
