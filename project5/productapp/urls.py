from django.urls import path
from productapp import views

urlpatterns = [
    path("product_list",views.product_list,name='product_list'),
    path("product_detail/<int:id>",views.product_detail,name='product_detail'),
    path("product_create/",views.product_create,name='product_create'),
    path('product_update/<int:id>/',views.product_update,name='product_update'),
    # path('product_delete/<int:id>/',views.product_delete,name='product_delete'),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete')

]