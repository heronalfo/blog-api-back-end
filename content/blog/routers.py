from rest_framework.routers import SimpleRouter
from blog.viewsets.posts_view_set import PostsViewSet

routers = SimpleRouter()

routers.register('posts/api/v1', PostsViewSet, basename='posts')

urlpatterns = routers