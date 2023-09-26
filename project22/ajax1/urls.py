from django.urls import path
from ajax1 import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('create',views.create,name='create'),

]
