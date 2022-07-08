from rest_framework import serializers
from likes_app.models import LikePost, LikeComment


class LikePostSerializer(serializers.ModelSerializer):
    """Serializer for likes posts."""

    class Meta:
        model = LikePost
        fields = '__all__'
        # read_only_fields = True

    # чтобы пользователь ничего не указывал
    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )


class LikeCommentSerializer(serializers.ModelSerializer):
    """Serializer for likes comments."""

    class Meta:
        model = LikeComment
        fields = '__all__'

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )

