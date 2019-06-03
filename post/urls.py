from django.urls import path,re_path

from .views import post_create,post_detail,post_update,PostList,PostDelete,UserProfile

app_name = 'post'
urlpatterns = [
    path('create/', post_create,name='create'),
    path('<slug:slug>/', post_detail, name='detail'),
    path('<slug:slug>/update/', post_update, name='update'),
   	path('', view=PostList.as_view(), name='list'),
    path('<slug:slug>/delete/', view=PostDelete.as_view(), name='delete'),
    path('@<username>/', view=UserProfile.as_view(), name="userPost"),
]