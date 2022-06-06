from django.shortcuts import render
from django.views import View

from first_app.models import Post, Tag


class Posts(View):

    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True)
        tags = Tag.objects.all()
        context = {
            'title': "Posts",
            'name_text': 'Publications',
            'posts': posts,
            'tag': tags
        }
        return render(request, 'posts.html', context)
