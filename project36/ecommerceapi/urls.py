from django.urls import path
from ecommerceapi import views



urlpatterns = [
    path("products_lists",views.list_products,name='products_lists'),
    # Sample Serializer Urls
    path("samplecomment",views.samplecomment,name='samplecomment'), 
    #classBasedViewsUrls
    path("products_list_api_view/",views.ProductListView.as_view(),name='products_list_api_view'),   
    path("products_detail_api_view/<int:pid>",views.ProductDetailView.as_view(),name='products_detail_api_view'),   


]
