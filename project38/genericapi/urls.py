from django.urls import path
from genericapi import views
from genericapi.views import EmployeeViewSets

from rest_framework.routers import DefaultRouter,SimpleRouter

router = DefaultRouter()
router.register(
    'employeeviewset',EmployeeViewSets,basename='employee'
)


urlpatterns = [
    # <-------------------Generic Views urls Started ------------->
    path("Employee_Generic_lists",views.EmployeeGerericView.as_view(),name='Employee_Generic_lists'),
    path("Employee_Generic_create",views.EmployeeGerericCreate.as_view(),name='Employee_Generic_create'),
    path("Employee_Generic_detail/<int:pk>",views.EmployeeGerericDetail.as_view(),name='Employee_Generic_detail'),

# <-------------------Generic Views urls Ended ------------->



]+router.urls