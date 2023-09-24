from django.shortcuts import get_object_or_404, redirect, render

from fieldsapp.models import UserProfile
from fieldsapp.forms import UserProfileForm

# Create your views here.

def user_profile_view(request):
    users = UserProfile.objects.all()
    return render(request,'fieldsapp/user_profiles.html',{'users':users})



def user_create_view(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profiles')
        
    return render(request,'fieldsapp/user_form.html',{'form':form})
    


def user_update_view(request,id):
    user = get_object_or_404(UserProfile, id=id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profiles')
    else:
        form = UserProfileForm(instance=user)
        addr = user.books_authored.all()
    
    return render(request,'fieldsapp/user_update.html',{'form':form,'addr':addr})



def user_delete_view(request,id):
    user = UserProfile.objects.get(id=id)
    user.delete()
    return redirect('user_profiles')
    







































