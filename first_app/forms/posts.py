from first_app.models import Post

from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'created_at']
