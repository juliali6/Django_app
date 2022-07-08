from rest_framework.mixins import DestroyModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from likes_app.api.serializers.likes import LikePostSerializer, LikeCommentSerializer
from likes_app.models import LikePost, LikeComment


class LikePostView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    """View for likes posts"""

    queryset = LikePost.objects.all()
    serializer_class = LikePostSerializer


class LikeCommentView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    """View for likes comments"""

    queryset = LikeComment.objects.all()
    serializer_class = LikeCommentSerializer

