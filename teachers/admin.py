from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(SortableAdminMixin, ModelAdmin):
    list_display = ('order', 'photo_preview', 'full_name', 'role', 'is_active')
    list_display_links = ('full_name',)
    list_filter = ('is_active',)
    search_fields = ('full_name', 'role', 'bio')
    prepopulated_fields = {'slug': ('full_name',)}
    filter_horizontal = ('courses',)

    fieldsets = (
        ("Asosiy", {"fields": ("full_name", "slug", "role", "bio")}),
        ("Rasm", {"fields": ("photo",)}),
        ("Kurslar", {"fields": ("courses",)}),
        ("Aloqa", {"fields": ("telegram", "linkedin")}),
        ("Ko'rinish", {"fields": ("is_active", "order")}),
    )

    @admin.display(description="Rasm")
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="40" height="40" style="object-fit:cover;border-radius:50%;">', obj.photo.url)
        return "—"
