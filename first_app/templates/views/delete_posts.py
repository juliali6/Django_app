from django.urls import reverse_lazy
from django.views.generic import DeleteView

from first_app.models import Post


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_posts.html'
    success_url = reverse_lazy('main_page')
