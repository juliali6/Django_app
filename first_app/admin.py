from django.contrib import admin

# Register your models here.
from first_app.models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title')  # ��������� ����� ���� ���������� �� �������� ������ ��������
    ordering = ('-created_at', '-id')  # ���������� �� ���������
    readonly_fields = ('created_at',)  # ���� �� �������� ��� ����������� ���������