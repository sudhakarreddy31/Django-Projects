from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from projectapp.models import Book

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'projectapp/book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'projectapp/book_detail.html'



class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'pages', 'price']
    template_name = '/home/sudhakarreddy/DjangoProjects/project1/projectapp/templates/projectapp/book_create.html'


class BookUpdateView(CreateView):
    model = Book
    fields = ['title', 'author', 'pages', 'price']
    template_name = 'projectapp/book_update.html'
    success_url = 'listview/'

    def get_object(self, queryset=None):
    # Retrieve the Book object based on the primary key (pk) from the URL
        return Book.objects.get(pk=self.kwargs['pk']) 


class BookDeleteView(DeleteView):
    model= Book 
    template_name = 'projectapp/company_delete.html'
    success_url = reverse_lazy('listview')
    


