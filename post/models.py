from django.db import models
from userprofiles.models import Profile


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    userPost = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
