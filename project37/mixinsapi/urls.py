from django.urls import path
from mixinsapi import views

urlpatterns = [
    path("employee_lists_mixins",views.ListEmployeeMixins.as_view(),name='employee_lists_mixins'),
    path("employee_details_mixins/<int:pk>/",views.EmployeeDetailMixins.as_view(),name='employee_detail_mixins'),
    path("employee_create_mixins",views.EmployeeCreateMixins.as_view(),name='employee_create_mixins'),
]