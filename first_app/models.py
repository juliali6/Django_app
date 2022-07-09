from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

from media_app.models import Media


class Post(models.Model):
    """Model for posts."""

    objects = None
    created_at = models.DateTimeField(auto_now_add=True)  # время создания публикации
    title = models.CharField(max_length=1000, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)  # по умолчанию публичный
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True, related_name='tag_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class ImagePost(models.Model):
    """Model for post images"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image_post')
    image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name='Photo')

    def get_absolute_url(self):
        return f'/image{self.id}'

    class Meta:
        verbose_name = 'Photo post'
        verbose_name_plural = 'Photo posts'


class Tag(models.Model):
    """Model for tags"""

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)