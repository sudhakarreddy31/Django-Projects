from django.urls import path
from fieldsapp import views


urlpatterns = [
    path('user_profiles',views.user_profile_view,name='user_profiles'),
    path('user_form',views.user_create_view,name='user_form'),
    path('user_update/<int:id>',views.user_update_view,name='user_update'),
    path('user_delete/<int:id>',views.user_delete_view,name='user_delete'),

]