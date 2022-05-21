from first_app.models import Post

from django.core.paginator import Paginator
from django.shortcuts import render


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all() # order_by = сортировка
    # posts = ({'title': random.randint(100, 1_000_000), 'text': 'Нужно еще больше текста'} for _ in range(100))
    # (создать посты не обращаясь к базе данных)
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'title': 'Hello TMS', 'posts': posts, 'page_obj': page_obj}
    return render(request, 'main_page.html', context)
