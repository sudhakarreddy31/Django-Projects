from django.urls import path

from multimodelsapp import views

urlpatterns = [
    path('customers_lists',views.customer_list,name='customers_lists'),
    path('customers_create',views.customer_create,name='customers_create'),
    path('customers_update/<int:id>',views.customer_update,name='customers_update'),
    path('customers_delete<int:id>',views.customer_delete,name='customers_delete'),

]
