from django.http import HttpRequest
from django.shortcuts import render

from ajax1.models import Profile

# Create your views here.
def index(request):

    return render(request,'ajax1/index.html')

def create(request):
    if request.method =='POST':
        full_name =request.POST['full_name']
        bio =request.POST['bio']
        email =request.POST['email']
        phone =request.POST['phone']

        new_profiles = Profile(full_name=full_name,bio=bio,email=email,phone=phone)
        new_profiles.save()
        success = 'Profile Created Sucessfully for ' + full_name
        return HttpRequest(success)