from django.urls import path,include

from ormsapp import views

urlpatterns = [
    path('employees',views.employee_view),
    path('aggrate',views.display_view),
    
]
