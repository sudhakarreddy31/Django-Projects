from django.urls import path
from apiapp import views

urlpatterns = [
    path('drinks',views.drink_lists),
    path('details/<int:id>',views.drink_details),
    
]
