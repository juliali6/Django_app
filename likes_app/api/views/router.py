from rest_framework import routers
from ..views.likes import LikeCommentView, LikePostView

api_router = routers.DefaultRouter()
api_router.register('likes', LikePostView, LikeCommentView)
