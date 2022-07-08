from django import forms
from first_app.models import Post


class PostFormCreate(forms.ModelForm):
    """Model form for creating a new post."""

    title = forms.CharField(max_length=30)
    text = forms.CharField(max_length=500)

    class Meta:
        model = Post
        fields = ['title', 'text']


class PostImageFormCreate(PostFormCreate):
    """Model form for creating a new post image."""

    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(PostFormCreate.Meta):
        fields = PostFormCreate.Meta.fields + ['image', ]


