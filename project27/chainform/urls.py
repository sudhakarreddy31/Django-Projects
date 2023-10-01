from django.urls import path
from chainform import views

urlpatterns = [
    path('person_list',views.PersonListView.as_view(),name='persons_list'),
    path('person_create',views.PersonCreateView.as_view(),name='person_create'),
    path('person_update/<int:id>/',views.PersonUpdateView.as_view(),name='person_update'),
    path('person_delete/<int:id>/',views.PersonDeleteView.as_view(),name='person_delete'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here

]
