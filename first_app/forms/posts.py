from django.forms import ModelForm, TextInput, Textarea
from first_app.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']