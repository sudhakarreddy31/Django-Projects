from django.urls import path
from crudinforms import views

urlpatterns = [
    path('employee_lists',views.employee_list,name='employee_lists'),
    path('employee_create',views.employee_create_view,name='employee_create'),
    path('employee_update/<int:id>',views.employee_update_view,name='employee_update'),
    path('employee_delete/<int:id>',views.employee_delete_view,name='employee_delete'),

]
