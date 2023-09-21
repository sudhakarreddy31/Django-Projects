from django.shortcuts import redirect, render
from abstactmultiapp.forms import BookForm

from abstactmultiapp.models import Book

# Create your views here.


def book_list(request):
    books = Book.objects.all()
    return render(request,'abstactmultiapp/book_list.html',{'books':books})


def book_create(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_lists')
    return render(request,'abstactmultiapp/book_create.html',{'form':form})


def book_update(request,id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_lists')
    else:
        form = BookForm(instance=book)
    return render(request,'abstactmultiapp/book_update.html',{'form':form})



def book_delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books_lists')





















