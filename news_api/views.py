from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Tag, Article, Comment, Author, Subscriber
from .serializers import CategorySerializer, TagSerializer, ArticleSerializer, CommentSerializer, AuthorSerializer, SubscribersSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'category__name': ['exact', 'icontains'],  # Use related field filtering
        'tags__name': ['exact', 'icontains'],
    }

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SubscribersViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscribersSerializer
