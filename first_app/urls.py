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
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from first_app.api.views.router import api_router
from first_app.templates.views.audio import upload_file
from first_app.templates.views.create_post import CreatePost
from first_app.templates.views.delete_posts import DeletePostView
from first_app.templates.views.posts import Posts

from first_app.templates.views.tags import tags_list, tag_detail
from first_app.templates.views.update_post import UpdatePostView
from first_app.templates.views.views import main_page
from views.main import PostListView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),
    path('create', CreatePost.as_view, name='create'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('create_posts/', PostListView.as_view(), name='create_posts'),
    path('api/', include(api_router.urls)),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>', tag_detail, name='tag_detail'),
    path('posts/', Posts.as_view(), name='posts'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
