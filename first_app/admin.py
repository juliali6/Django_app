from django.contrib.auth.admin import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User
from .models import Profile, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title',)  # ��������� ����� ���� ���������� �� �������� ������ ��������
    ordering = ('-created_at', '-id')  # ���������� �� ���������
    readonly_fields = ('created_at',)  # ���� �� �������� ��� ����������� ���������


admin.site.unregister(User)


class ProfileInLine(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = [
        ProfileInLine
    ]
