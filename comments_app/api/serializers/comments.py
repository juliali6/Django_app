from rest_framework import serializers
from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comments."""

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['User']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )
