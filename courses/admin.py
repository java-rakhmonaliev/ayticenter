from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import Course


@admin.register(Course)
class CourseAdmin(SortableAdminMixin, ModelAdmin):
    list_display = ('order', 'icon_emoji', 'name', 'level', 'price', 'is_active', 'cover_preview')
    list_display_links = ('name',)
    list_filter = ('level', 'is_active')
    search_fields = ('name', 'tagline', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active',)

    fieldsets = (
        ("Asosiy", {"fields": ("name", "slug", "icon_emoji", "tagline", "description")}),
        ("Rasm", {"fields": ("cover_image",)}),
        ("Jadval va narx", {"fields": ("duration", "schedule", "price", "level")}),
        ("Ko'rinish", {"fields": ("badge_text", "is_active", "order")}),
    )

    @admin.display(description="Cover")
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="50" height="35" style="object-fit:cover;border-radius:4px;">', obj.cover_image.url)
        return format_html('<span style="font-size:24px">{}</span>', obj.icon_emoji)
