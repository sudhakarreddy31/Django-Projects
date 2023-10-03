from django.urls import path
from testing import views

urlpatterns = [
    path('list',views.ItemListView.as_view(),name='items_lists'),
    path('list_create/',views.ItemCreateView.as_view(),name='item_create'),
    path('list_update/<int:id>/',views.ItemUpdateView.as_view(),name='item_update'),
    path('list_delete/<int:id>/',views.ItemDeleteView.as_view(),name='item_delete'),

]
