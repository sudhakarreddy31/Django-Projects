from rest_framework import routers
from webmoblieapi.viewsets import EmployeeViewset


router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)
