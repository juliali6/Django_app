from django.views.generic import ListView

from comments_app.models import Comment
from first_app import models
from first_app.models import Post
from django.shortcuts import render


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()  # order_by = сортировка
    # posts.py = ({'title': random.randint(100, 1_000_000), 'text': 'Нужно еще больше текста'} for _ in range(100))
    # (создать посты не обращаясь к базе данных)

    context = {'title': 'Hello TMS', 'posts.py': posts}
    return render(request, 'main_page.html', context)


class PostListView(ListView):
    queryset = Post.objects.order_by('-created_at', '-id')
    template_name = 'main_page.html'
    context_object_name = 'posts.py'
    http_method_names = ['get']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset

        return self.queryset.filter(is_public=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Posts through ListView'
        return context

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        return result

    def post(self, request, *args, **kwargs):
         pass
