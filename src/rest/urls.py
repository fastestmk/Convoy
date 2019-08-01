from django.urls import path

from .views import post_detail, posts_api

app_name = "Api"
urlpatterns = [
    path("posts_api/", view=posts_api, name="posts_api"),
    path("posts_api/<int:pk>/", view=post_detail),
]
