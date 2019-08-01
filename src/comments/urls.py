from django.urls import path

from .views import comment_delete, comment_thread

app_name = "comments"
urlpatterns = [
    path("<int:id>/", comment_thread, name="thread"),
    path("<int:id>/delete/", comment_delete, name="delete"),
]
