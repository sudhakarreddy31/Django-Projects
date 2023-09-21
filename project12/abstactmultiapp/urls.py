from django.urls import path
from abstactmultiapp import views

urlpatterns = [
    path('books_lists',views.book_list,name='books_lists'),
    path('book_create',views.book_create,name='book_create'),
    path('book_update/<int:id>',views.book_update,name='book_update'),
    path('book_delete/<int:id>',views.book_delete,name='book_delete'),

    


]