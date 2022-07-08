from rest_framework import serializers
from friends_app.models import Friendship


class FriendshipSerializer(serializers.ModelSerializer):
    """Serializer for friendship."""

    class Meta:
        model = Friendship
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )
