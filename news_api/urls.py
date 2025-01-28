from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet, ArticleViewSet, CommentViewSet, SubscribersViewSet, AuthorsViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'authors', AuthorsViewSet)
router.register(r'subscribers', SubscribersViewSet)

urlpatterns = router.urls

