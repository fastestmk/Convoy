from django.urls import path,re_path

from .views import post_list,post_create,post_detail,post_update,post_delete

app_name = 'post'
urlpatterns = [
	path('', post_list, name='list'),
    path('create/', post_create,name='create'),
    path('<slug:slug>/', post_detail, name='detail'),
    path('<slug:slug>/update/', post_update, name='update'),
    path('<slug:slug>/delete/', post_delete, name='delete'),
]
