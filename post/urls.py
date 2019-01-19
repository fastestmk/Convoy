from django.urls import path
from .views import PostList, NewPost, PostDetail, CommentView, PostDelete, PostEdit, userPost, searchPost

app_name = 'post'
urlpatterns = [
    path('', view=PostList, name='list'),
    path('add/', view=NewPost.as_view(), name='add'),
    path('detail/<int:pk>/', view=PostDetail, name='detail'),
    path('detail/<int:pk>/comment/', view=CommentView.as_view(), name='comment'),
    path('edit/<int:pk>/', view=PostEdit.as_view(), name='edit'),
    path('delete/<int:pk>/', view=PostDelete, name='delete'),
    path('<username>/', view=userPost, name="userPost"),
    path('SearchPost/', view=searchPost, name='searchPost'),
]
