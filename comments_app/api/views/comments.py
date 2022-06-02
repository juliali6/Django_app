from rest_framework.filters import OrderingFilter
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from comments_app.api.serializers.comments import CommentSerializer
from comments_app.models import Comment


class CommentView(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [OrderingFilter]

