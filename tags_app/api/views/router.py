from rest_framework import routers

from ..views.tags import TagViewSet

api_router = routers.DefaultRouter()
api_router.register('tags', TagViewSet)
