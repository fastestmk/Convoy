from django.urls import path

from .views import posts_api

app_name = 'Api'
urlpatterns = [
    path('posts_api/', view=posts_api, name='posts_api'),
]
