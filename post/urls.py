from django.urls import path
from .views import PostList, NewPost, PostDetail, CommentView

app_name = 'post'
urlpatterns = [
    path('', view=PostList, name='list'),
    path('add/', view=NewPost.as_view(), name='add'),
    path('detail/<int:pk>/', view=PostDetail.as_view(), name='detail'),
    path('detail/<int:pk>/comment/', view=CommentView.as_view(), name='comment'),
]
