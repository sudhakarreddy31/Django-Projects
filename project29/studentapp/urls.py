from django.urls import path,include
from studentapp import views

urlpatterns = [
    path('home',views.StudentListView.as_view(),name='student_lists'),
    path("register",views.RegistrationView.as_view(),name='registration'),
    path("login",views.LoginView.as_view(),name='login'),
    path("student_lists",views.StudentListView.as_view(),name='student_lists'),
    path("student_form",views.StudentCreateView.as_view(),name='student_form'),
    path("student_update/<int:id>",views.StudentUpdateView.as_view(),name='student_update'),
    path("student_delete/<int:id>",views.StudentDeleteView.as_view(),name='student_delete'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]
