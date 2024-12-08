from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'state', 'created', 'modified')
    list_filter = ('status', 'state', 'created')
    search_fields = ('title', 'content')
