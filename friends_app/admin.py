from django.contrib import admin
from .models import Friendship


@admin.register(Friendship)
class FriendsAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender', 'receiver']

    class Meta:
        model = Friendship

