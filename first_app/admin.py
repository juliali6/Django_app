from django.contrib.auth.admin import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User
from .models import Profile, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title',)  # указывает какие поля отображать на странице списка объектов
    ordering = ('-created_at', '-id')  # сортировка по умолчанию
    readonly_fields = ('created_at',)  # поле на просмотр без возможности изменения


admin.site.unregister(User)


class ProfileInLine(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = [
        ProfileInLine
    ]
