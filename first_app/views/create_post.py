from django.shortcuts import render, redirect
from django.views import View

from first_app.forms.create_posts import PostImageFormCreate
from first_app.models import ImagePost


class CreatePost(View):
    @staticmethod
    def get(request):
        form = PostImageFormCreate()
        context = {
            'title': 'Add post',
            'create_post': form,
        }
        return render(request, 'create_post.html', context)

    @staticmethod
    def post(request):
        form_image = PostImageFormCreate(request.POST, request.FILES)
        files = request.FILES.getlist('image')

        if len(files) > 4:
            return render(request, 'create_post.html', context={
                'title': 'Add Post',
                'form': form_image,
                'error': 'Maximum 4 files!'
            })

        if form_image.is_valid():
            post_object = form_image.save(commit=False)
            post_object.user = request.user
            post_object.save()
            for f in files:
                ImagePost.objects.create(post=post_object, image=f)
            return redirect('/')

        context = {
            'create_post': form_image,
        }
        return render(request, 'main_page.html', context)

