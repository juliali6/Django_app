from django.contrib.auth.admin import admin
from django.contrib.auth.models import User

from first_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title',)
    ordering = ('-created_at', '-id')
    readonly_fields = ('created_at', 'image_tag')


admin.site.unregister(User)
