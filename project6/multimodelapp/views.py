from django.shortcuts import redirect, render
from multimodelapp.models import Book
from multimodelapp.forms import BookForm


# Create your views here.
def book_lists(request):
    books = Book.objects.all()
    return render(request,'multimodelapp/book_list.html',{'books':books})


# def create_book(request):
#     form = BookForm()
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/books_lists')
#     return render(request,'multimodelapp/create_book.html',{'form':form})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_lists')
    else:
        form = BookForm()
        print(form.errors)        
        
    return render(request,'multimodelapp/create_book.html',{'form':form})


def update_book(request,id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = Book(request.POST,instance=book)
        if form.is_valid():
            form.save()
        return redirect('books_lists')
    else:
        form=BookForm(instance=book)
    return render(request,'multimodelapp/update_book.html',{'book':book,'form':form})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('/books_lists')
    return render(request, 'multimodelapp/delete_book.html', {'book': book})


