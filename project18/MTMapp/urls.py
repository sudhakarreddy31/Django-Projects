from django.urls import path,include

from MTMapp import views

urlpatterns = [
    path('product_lists',views.products_list,name='product_lists'),
    path('product_create',views.product_create,name='product_create'),
    path('product_update/<int:id>',views.product_update,name='product_update'),
    path('product_delete/<int:id>',views.product_delete,name='product_delete'),

]
