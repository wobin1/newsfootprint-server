from rest_framework import serializers
from .models import Category, Tag, Article, Comment, Author, Subscriber

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
        fields = '__all__'  # Include all fields by default

class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'  # Include all fields by default


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = serializers.StringRelatedField()
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'
