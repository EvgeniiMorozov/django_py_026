from django.contrib import admin

from .models import PostModel, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "text", "image", "publish_date", "is_published")
    list_display_links = ("id", "author")
    search_fields = ("title", "text")
    list_editable = ("is_published", "title", "text")
    list_filter = ("is_published", "publish_date")
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(PostModel, PostAdmin)
admin.site.register(Category, CategoryAdmin)
