from django.urls import path
from .views import PostList, NewPost, PostDetail, CommentView, PostDelete, PostEdit, searchPost, UserProfile, post

app_name = 'post'
urlpatterns = [
    path('', view=PostList.as_view(), name='list'),
    path('add/', view=NewPost.as_view(), name='add'),
    path('detail/<int:pk>/', view=PostDetail.as_view(), name='detail'),
    path('detail/<int:pk>/comment/', view=CommentView.as_view(), name='comment'),
    path('edit/<int:pk>/', view=PostEdit.as_view(), name='edit'),
    path('delete/<int:pk>/', view=PostDelete.as_view(), name='delete'),
    path('@<username>/', view=UserProfile.as_view(), name="userPost"),
    path('SearchPost/', view=searchPost, name='searchPost'),
    path('detail/<int:pk>/post/', view=post, name='post'),
]
