from django.urls import path
from dropdownlist import views

urlpatterns = [
    path('studentlist',views.StudentListView.as_view(),name='student_lists'),
    path('studentcreate/', views.StudentCreateView.as_view(), name='student_create'),
    path('student_update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student_delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
]
