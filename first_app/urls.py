"""z22django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from first_app.api.views.router import api_router
from first_app.views.create_post import CreatePost
from first_app.views.delete_posts import delete_post
from first_app.views.main import PostListView
from first_app.views.posts import Posts
from first_app.views.tags import tags_list, tag_detail
from first_app.views.views import MainPage

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main_page'),
    path('create_post/', login_required(CreatePost.as_view()), name='create_post'),
    path('posts_list/', PostListView.as_view(), name='posts_list'),
    path('api/', include(api_router.urls)),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>', tag_detail, name='tag_detail'),
    path('posts/', Posts.as_view(), name='posts'),
    path('delete/<int:pk>/', login_required(delete_post), name='delete_post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
