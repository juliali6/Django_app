from django.core.paginator import Paginator
from django.views import View
from django.views.generic import ListView
from first_app.models import Post

from django.shortcuts import render, redirect


class MainPage(View):
    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()
        # create_posts.py = ({'title': random.randint(100, 1_000_000), 'text': ''} for _ in range(100))
        # contact_list = Post.objects.all()
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'title': 'Hello TMS', 'posts': page_obj}
        return render(request, 'main_page.html', context)


class PostListView(ListView):
    paginate_by = 3
    model = Post

    queryset = Post.objects.order_by('-created_at', '-id')
    template_name = 'main_page.html'
    context_object_name = 'create'
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


