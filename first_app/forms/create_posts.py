from django import forms
from first_app.models import Post


class PostFormCreate(forms.ModelForm):
    title = forms.CharField(max_length=30)
    text = forms.CharField(max_length=500)

    class Meta:
        model = Post
        fields = ['title', 'text']


class PostImageFormCreate(PostFormCreate):
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(PostFormCreate.Meta):
        fields = PostFormCreate.Meta.fields + ['image', ]


