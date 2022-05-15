
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ProfileEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')