from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'article_title',
        'article_text',
        'article_date'
    ]
    list_filter = ['article_date']

admin.site.register(Article, ArticleAdmin)
