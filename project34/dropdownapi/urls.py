from django.urls import path
from dropdownapi import views

urlpatterns = [
    path('countries/', views.CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<int:country_id>/cities/', views.CityListCreateView.as_view(), name='city-list-create'),
    path('persons/', views.PersonListCreateView.as_view(), name='student-list-create'),
    path('persons/<int:pk>/', views.PersonDetailView.as_view(), name='student-detail'),

]
