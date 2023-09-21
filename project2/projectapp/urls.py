from django.urls import path
from projectapp import views

urlpatterns = [
    path("listview",views.CompanyListView.as_view(),name='listview'),
    path("detailview/<int:pk>/",views.CompanyDetailView.as_view(),name='detailview'),
    path("createview/",views.CompanyCreateView.as_view()),
    path("updateview/<int:pk>/",views.CompanyUpdateView.as_view()),
    path("deleteview/<int:pk>/",views.CompanyDeleteView.as_view())


]
