from django.contrib.auth.models import User
from django.forms import ModelForm


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)  # не сохраняет пользователя в базе данных
        user.set_password(self.cleaned_data['password'])  # хэширование пароля
        if commit:
            user.save()

        return user
