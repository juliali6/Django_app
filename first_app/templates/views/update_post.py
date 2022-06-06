from django.views.generic import UpdateView

from first_app.models import Post


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_posts.html'
    fields = ['title', 'text']
