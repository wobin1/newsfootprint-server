from rest_framework import serializers
from .models import Category, Tag, Article, Comment, Author
import django_filters

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__' 


class ArticleSerializer(serializers.ModelSerializer):
    tags = django_filters.CharFilter(field_name='tags__name', lookup_expr='icontains')
    category = serializers.StringRelatedField()
    tags = TagSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'
