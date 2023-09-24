from django.urls import  path

from registerform import views

urlpatterns = [
    path('register_form',views.register_form),
    path('login_form',views.login_form,name='loginform'),
    
]
