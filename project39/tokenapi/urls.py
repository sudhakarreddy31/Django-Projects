from django.urls import path
from tokenapi import views




urlpatterns = [
    path("bikelists",views.BikeListView.as_view(),name='bikelists'),
    path("bikedetail/<int:pk>",views.BikeDetailView.as_view(),name='bikedetail'),
    path("bikecreate",views.BikeCreateView.as_view(),name='bikecreate'),
    path("bikeupdate/<int:pk>",views.BikeUpdateView.as_view(),name='bikeupdate'),
    path("bikedelete/<int:pk>",views.BikeDeleteView.as_view(),name='bikedelete'),

]
