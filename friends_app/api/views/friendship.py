from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ...models import Friendship
from ..serializers.friendship import FriendshipSerializer


class FriendsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
