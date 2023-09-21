from django.urls import include, path

from prefetch_related import views

urlpatterns = [
    path('index',views.index),

]