from rest_framework import serializers

from comments_app.api.serializers.comments import CommentSerializer
from media_app.api.serializers.media import MediaSerializer
from tags_app.api.serializers.tags import TagSerializer
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    """Model serializer for post."""

    class Meta:
        model = Post
        exclude = ['is_public']
        read_only_fields = ('id', 'user', 'is_public')
        extra_kwargs = {
            'file': {
                'required': True,
                'write_only': True,
                'help_text': 'ID media file'
            }
        }

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )
    # media = serializers.URLField(source='file.file.url', read_only=True)
    media = MediaSerializer(source='file', allow_null=False, read_only=True)
    tag = TagSerializer(many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes(self, instance) -> int:
        return instance.like.count()

    # def get_comment(self, instance) -> int:
    #     return instance.comment.count()
    #