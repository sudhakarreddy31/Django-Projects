# urls.py
from django.urls import path
from .views import (
    UniversityListView, UniversityDetailView, UniversityCreateView,
    UniversityUpdateView, UniversityDeleteView,
    StudentListView, StudentDetailView, StudentCreateView,
    StudentUpdateView, StudentDeleteView,
)

urlpatterns = [
    # University URLs
    path('universities/', UniversityListView.as_view(), name='university-list'),
    path('university/<int:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('university/add/', UniversityCreateView.as_view(), name='university-add'),
    path('university/<int:pk>/update/', UniversityUpdateView.as_view(), name='university-update'),
    path('university/<int:pk>/delete/', UniversityDeleteView.as_view(), name='university-delete'),

    # Student URLs
    path('students/', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/add/', StudentCreateView.as_view(), name='student-add'),
    path('student/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]
