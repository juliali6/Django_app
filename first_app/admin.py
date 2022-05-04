from django.contrib import admin

# Register your models here.
from first_app.models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title')  # указывает какие поля отображать на странице списка объектов
    ordering = ('-created_at', '-id')  # сортировка по умолчанию
    readonly_fields = ('created_at',)  # поле на просмотр без возможности изменения