from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User

from profile_app.models import Profile


class ProfileInLine(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = [
        ProfileInLine
    ]

