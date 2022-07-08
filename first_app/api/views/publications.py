from rest_framework import filters
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, \
    RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.publications import PostSerializer
from ...models import Post


class PostsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin,
                   RetrieveModelMixin):
    """View set for posts with using mixins."""

    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'id']
    search_fields = ['id', 'title', 'text', 'user__username']
