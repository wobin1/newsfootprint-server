# news/admin.py
from django.contrib import admin
from .models import Article, Category, Tag

admin.site.site_header = "News Footprint Administration"  # Top header
admin.site.site_title = "News Footprint Admin Portal"     # Browser tab title
admin.site.index_title = "Welcome to News footprint Admin"  # Dashboard title

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'published_at')
    search_fields = ('title', 'slug', 'content')
    list_filter = ('category', 'tags')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email')
#     search_fields = ('name', 'email')