from django.urls import path
from apiapp import views

urlpatterns = [
    path("stanger_lists",views.StrnagerListView.as_view(),name='stanger_lists'),
    path("stanger_create",views.StrnagerCreateView.as_view(),name='stanger_create'),
    path("stanger_update/<int:pk>/",views.StrnagerUpdateView.as_view(),name='stanger_update'),
    path("stanger_delete/<int:pk>/",views.StrnagerDeleteView.as_view(),name='stanger_delete'),


]