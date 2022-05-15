from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Post(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True)  # время создания публикации
    title = models.CharField(max_length=1000, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)  # по умолчанию публичный
    image = models.ImageField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(blank=True, null=True)
    phone = models.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        max_length=17,
        blank=True,
        null=True
    )
    about = models.TextField(max_length=4096, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    f_app = models.ForeignKey('User', on_delete=models.CASCADE)

