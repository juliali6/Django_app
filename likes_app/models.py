from django.contrib.auth.models import User
from django.db import models

from comments_app.models import Comment
from first_app.models import Post


class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_like')
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'like_post'),)


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_like')
    like_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'like_comment'),)

