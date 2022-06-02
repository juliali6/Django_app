from django.shortcuts import render

from first_app.models import Post
from tags_app.models import Tag


# def posts_list(request):
#     posts = Post.objects.all()
#     return render(request, 'main_page.html', context={'posts': posts})
#     # return HttpResponse("<h1>Hello! Hello!</h1>")


# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'tag_detail.html', context={'tag': tag})
