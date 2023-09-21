from django.urls import path
from abstractmethodsapp import views


urlpatterns = [
    path('lists',views.post_list,name='posts'),
    path('details/<int:id>',views.post_detail,name='details'),
    path('create',views.post_create,name='create_post'),
    path('update/<int:id>',views.post_update,name='post_update'),
    path('delete/int:id>',views.post_delete,name='post_delete')

]