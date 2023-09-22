from django.urls import path
from actressapp import views

urlpatterns = [
    path('movies_list',views.movies_list,name='movies_list'),
    path('movies_create',views.movie_create,name='movies_create'),
    path('movies_update/<int:id>',views.movie_update,name='movies_update'),
    path('movies_delete/<int:id>',views.movie_delete,name='movies_delete'),
    

]
