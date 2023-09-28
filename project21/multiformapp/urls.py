from django.urls import path,include

from multiformapp import views

urlpatterns = [
    path("firstpage",views.firstpage_view,name='firstpage'),
    path("secondpage",views.secondpage_view,name='secondpage'),
    path("thankyou",views.thankyou,name='thankyou'),
]
