from django.shortcuts import render
from movieapp.models import Movie
from django.views.generic import ListView,DetailView

# Create your views here.

class MovieListview(ListView):
    model = Movie
    template_name = 'movieapp/movie_list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movieapp/movie_detail.html'

class Movie



