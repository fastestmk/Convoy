from django.urls import path

from .views import (PostCreate, PostDelete, PostList, PostUpdate, UserProfile,
                    get_post_from_topic, post_detail)

app_name = "post"
urlpatterns = [
    path("create/", PostCreate.as_view(), name="create"),
    path("<slug:slug>/", post_detail, name="detail"),
    path("<slug:slug>/update/", PostUpdate.as_view(), name="update"),
    path("", PostList.as_view(), name="list"),
    path("<slug:slug>/delete/", PostDelete.as_view(), name="delete"),
    path("@<username>/", UserProfile.as_view(), name="userPost"),
    path("t/<slug:slug>", get_post_from_topic, name="get_post_from_topic"),
]
