from django.contrib.auth.models import User
from django.db import models

from first_app.models import Post


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

