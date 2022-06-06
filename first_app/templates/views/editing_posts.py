# from django.contrib import messages
# from django.shortcuts import get_object_or_404, render
#
# from first_app.forms.create_posts import PostFormCreate
# from first_app.models import Post
#
#
# def edit_post(request, pk):
#     template = 'first_app/create_post.html'
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         form = PostFormCreate(request.POST, instance=post)
#
#         try:
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'your post has been updated')
#
#         except Exception as e:
#             messages.warning(request, 'Your post was not saved do to an error: {}'.format(e))
#
#     else:
#         form = PostFormCreate(instance=post)
#
#     context = {
#         'from': form,
#         'post': post,
#     }
#
#     return render(request, template, context)

