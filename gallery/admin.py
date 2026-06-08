from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(SortableAdminMixin, ModelAdmin):
    list_display = ('order', 'thumbnail', 'caption', 'taken_at')
    list_display_links = ('caption',)
    search_fields = ('caption',)

    fieldsets = (
        ("Rasm", {"fields": ("image", "caption", "taken_at")}),
        ("Tartiblash", {"fields": ("order",)}),
    )

    @admin.display(description="Rasm")
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="60" style="object-fit:cover;border-radius:4px;">', obj.image.url)
        return "—"
