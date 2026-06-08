from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'published_at', 'is_published', 'cover_preview')
    list_display_links = ('title',)
    list_filter = ('is_published', 'published_at')
    search_fields = ('title', 'body')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'

    fieldsets = (
        ("Asosiy", {"fields": ("title", "slug", "body")}),
        ("Media", {"fields": ("cover_image",)}),
        ("Nashr", {"fields": ("published_at", "is_published")}),
    )

    @admin.display(description="Cover")
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover;border-radius:4px;">', obj.cover_image.url)
        return "—"
