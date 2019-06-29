from django.urls import path,re_path

from .views import PostCreate,post_detail,PostUpdate,PostList,PostDelete,UserProfile

app_name = 'post'
urlpatterns = [
    path('create/', view=PostCreate.as_view(),name='create'),
    path('<slug:slug>/',post_detail, name='detail'),
    path('<slug:slug>/update/', view=PostUpdate.as_view(), name='update'),
   	path('', view=PostList.as_view(), name='list'),
    path('<slug:slug>/delete/', view=PostDelete.as_view(), name='delete'),
    path('@<username>/', view=UserProfile.as_view(), name="userPost"),
]