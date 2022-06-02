from django.db.models.signals import post_save
from django.dispatch import receiver

from first_app.models import Post
import re

from tags_app.models import Tag


@receiver(post_save, sender=Post)
def created_tags(sender, instance, created, *args, **kwargs):
    for tag_name in re.findall(r'#(\w+)', instance.text):
        tag, is_created = Tag.objects.get_or_create(name=tag_name).lower()
        tag.posts.add(instance)
