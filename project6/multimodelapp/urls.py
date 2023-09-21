from django.urls import path
from multimodelapp import views

urlpatterns = [
    path('books_lists',views.book_lists,name='books_lists'),
    path('create_book',views.create_book,name='create_book'),
    path('update_book/<int:id>',views.update_book,name='update_book'),
    path('delete_book/<int:id>',views.delete_book,name='delete_book')
]