from django.urls import path
from decoratorapi import views


urlpatterns = [
    path("students",views.student,name='student_list'),
    path("login",views.login),
]
