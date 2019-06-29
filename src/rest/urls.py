from django.urls import path

from .views import posts_api, post_detail

app_name = 'Api'
urlpatterns = [
    path('posts_api/', view=posts_api, name='posts_api'),
    path('posts_api/<int:pk>/', view=post_detail),
]
