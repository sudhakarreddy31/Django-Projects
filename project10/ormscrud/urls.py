from django.urls import path

from ormscrud import views

urlpatterns = [
    path('list',views.employee_list),



]