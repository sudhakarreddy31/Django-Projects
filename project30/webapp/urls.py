from django.urls import path
from webapp import views

urlpatterns = [
    path('employee_list',views.EmployeeListView.as_view(),name='employees_lists'),
    path('employee_list/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),

]
