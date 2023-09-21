from django.urls import path
from projectapp import views

urlpatterns = [
    path("listview/",views.BookListView.as_view(),name='listview'),
    path("detailview/<int:pk>/",views.BookDetailView.as_view(),name='details'),
    path("createview/",views.BookCreateView.as_view(),name='createview'),
    path("updateview/<int:pk>/",views.BookUpdateView.as_view(),name='updateview'),
    path("deleteview/<int:pk>/",views.BookDeleteView.as_view(),name='deleteview')



]