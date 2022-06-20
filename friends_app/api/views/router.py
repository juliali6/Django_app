from rest_framework import routers

from friends_app.api.views.friendship import FriendsViewSet

api_router = routers.DefaultRouter()
api_router.register('friends', FriendsViewSet)
