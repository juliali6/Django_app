from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

from media_app.models import Media


class Post(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True)  # время создания публикации
    title = models.CharField(max_length=1000, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)  # по умолчанию публичный
    file = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True, related_name='tag_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # voice = models.FileField(upload_to='uploads/')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class AudioStore(models.Model):
    record = models.FileField(upload_to='media/')

    class Meta:
        db_table = 'Audio_store'
