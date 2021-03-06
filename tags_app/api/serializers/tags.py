from rest_framework import serializers

from ...models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, instance):
        return instance.posts.count()


