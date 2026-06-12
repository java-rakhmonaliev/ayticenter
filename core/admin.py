from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    fieldsets = (
        ("Hero", {"fields": ("hero_headline", "hero_sub", "hero_typed_words")}),
        ("Haqida", {"fields": ("about_text",)}),
        ("Aloqa", {"fields": ("address", "phone", "working_hours")}),
        ("Ijtimoiy tarmoqlar", {"fields": ("telegram_url", "instagram_url")}),
        ("Xarita", {"fields": ("google_maps_embed_url",)}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
