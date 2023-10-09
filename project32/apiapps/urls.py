from django.urls import path
from apiapps import views

urlpatterns = [
    path("tasks_lists",views.task_lists,name='tasks_lists'),
    path("tasks_detail/<str:pk>/",views.task_detail,name='tasks_detail'),
    path("tasks_create",views.task_create,name='tasks_create'),   
    path("tasks_update/<str:pk>/",views.task_update,name='tasks_update'),    
    path("tasks_delete/<str:pk>/",views.task_delete,name='tasks_delete'),    




]