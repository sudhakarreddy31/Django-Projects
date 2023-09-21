from django.shortcuts import render

from prefetch_related.models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().prefetch_related('store_set')
    for book in books:
        print(book.name,book.store_set.all())

    return None
