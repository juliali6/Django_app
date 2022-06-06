from django.shortcuts import render
from tags_app.models import Tag


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'tag_detail.html', context={'tag': tag})
