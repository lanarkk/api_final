from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1router = SimpleRouter()
v1router.register('posts', PostViewSet, basename='posts')
v1router.register('groups', GroupViewSet, basename='groups')
v1router.register('follow', FollowViewSet, basename='follow')
v1router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

version_one_urls = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(v1router.urls)),
]

urlpatterns = [
    path('v1/', include(version_one_urls))
]
