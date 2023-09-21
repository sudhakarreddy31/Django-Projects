from django.urls import path
from crudfbvapp import views

urlpatterns = [
    path('read/',views.read_view),
    path('create/',views.create_view),
    path('delete/<int:id>/', views.delete_view),
    path('update/<int:id>/', views.update_view,name='update_employee'),

    
    ]
