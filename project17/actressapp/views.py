from django.shortcuts import get_object_or_404, redirect, render
from .models import Actress,Movie,Director
from actressapp.forms import MovieForm


# Create your views here.
def movies_list(request):
    movies = Movie.objects.all()
    return render(request,'actressapp/movies_list.html',{'movies':movies})


def movie_create(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies_list')
    
    return render(request,'actressapp/movies_create.html',{'form':form})


def movie_update(request,id):
    movie = get_object_or_404(Movie,id=id)
    if request.method == 'POST':
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid:
            form.save()
            return redirect('movies_list')
    else:
        form = MovieForm(instance=movie)
        actresses = movie.actresses.all()
        
    return render(request,'actressapp/movies_update.html',{'form':form,'actresses':actresses,'movie':movie})

def movie_delete(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('movies_list')

