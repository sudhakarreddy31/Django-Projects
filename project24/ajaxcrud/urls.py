from django.urls import path
from ajaxcrud import views
from ajaxcrud.views import StudentInfoCreateView, StudentInfoDeleteView, StudentInfoListView, StudentInfoUpdateView

urlpatterns = [
    path("studentlists/", StudentInfoListView.as_view(), name='studentslists'),
    path("studentcreate/", StudentInfoCreateView.as_view(), name='student_create'),  # Note the trailing slash
    path('studentupdate/<int:pk>/', StudentInfoUpdateView.as_view(), name='studentupdate'),
    path('studentdelete/<int:pk>/', StudentInfoDeleteView.as_view(), name='studentdelete'),



    
]