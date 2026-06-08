from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    list_display = ('full_name', 'phone', 'course', 'status', 'submitted_at')
    list_display_links = ('full_name',)
    list_filter = ('status', 'course', 'submitted_at')
    search_fields = ('full_name', 'phone')
    list_editable = ('status',)
    readonly_fields = ('submitted_at',)
    date_hierarchy = 'submitted_at'

    fieldsets = (
        ("Ariza", {"fields": ("full_name", "phone", "course", "message", "submitted_at")}),
        ("Admin", {"fields": ("status", "admin_note")}),
    )
