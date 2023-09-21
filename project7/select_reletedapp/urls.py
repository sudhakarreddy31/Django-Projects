from django.urls import include, path
from select_reletedapp import views

urlpatterns = [
    path("home",views.home),
    path("index",views.index),
    path('select',views.select),
    path('selec',views.selec),

]
