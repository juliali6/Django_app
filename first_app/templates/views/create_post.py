from django.shortcuts import render, redirect
from django.views import View

from first_app.forms.create_posts import PostFormCreate


class CreatePost(View):
    @staticmethod
    def get(request):
        form = PostFormCreate()
        context = {
            'create_post': form,
        }
        return render(request, 'create_post.html', context)

    @staticmethod
    def post(request):
        form = PostFormCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'create_post': form,
        }
        return render(request, 'create_post.html', context)
