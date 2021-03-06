from django.db import models

from first_app.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')
