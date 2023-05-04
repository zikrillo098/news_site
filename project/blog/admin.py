from django.contrib import admin
from .models import Article, Category, CustomUser


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'created_at', 'update_at', 'is_published', 'photo')
    list_editable = ('is_published',)
    list_display_links = ('title', 'pk')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(CustomUser)
