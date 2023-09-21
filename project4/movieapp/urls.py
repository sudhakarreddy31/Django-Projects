from django.urls import path
from movieapp import views

urlpatterns = [
    path('list_view',views.MovieListview.as_view()),
    path('detail_view',views.DetailView.as_view()),

]
