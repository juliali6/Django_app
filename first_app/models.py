from django.db import models


class Post(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True)  # ����� �������� ����������
    title = models.CharField(max_length=1000, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)  # �� ��������� ���������