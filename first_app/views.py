import random

from django.shortcuts import render

from first_app.models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()  # order_by = сортировка
    # posts = ({'title': random.randint(100, 1_000_000), 'text': 'Нужно еще больше текста'} for _ in range(100))
    # (создать посты не обращаясь к базе данных)

    context = {'title': 'Hello TMS', 'posts': posts}
    return render(request, 'main_page.html', context)