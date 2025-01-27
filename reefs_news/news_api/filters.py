import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(field_name='tags__name', lookup_expr='icontains')  # Filter by tag name
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')  # Filter by tag name

    class Meta:
        model = Article
        fields = ['id', 'tags', 'title', 'is_published', 'category']
