from django.urls import path

from .views import CommentDelete, comment_thread

app_name = "comments"
urlpatterns = [
    path("<int:id>/", comment_thread, name="thread"),
    path("<int:id>/delete/", CommentDelete.as_view(), name="delete"),
]
