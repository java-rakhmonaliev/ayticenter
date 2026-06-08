from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, StackedInline
from adminsortable2.admin import SortableAdminMixin
from .models import CareerPath, CareerCompany


class CareerCompanyInline(StackedInline):
    model = CareerCompany
    extra = 1
    fields = ('name', 'logo')


@admin.register(CareerPath)
class CareerPathAdmin(SortableAdminMixin, ModelAdmin):
    list_display = ('order', 'job_title', 'course', 'avg_salary_range')
    list_display_links = ('job_title',)
    list_filter = ('course',)
    search_fields = ('job_title', 'description')
    inlines = [CareerCompanyInline]

    fieldsets = (
        ("Asosiy", {"fields": ("course", "job_title", "description", "avg_salary_range")}),
        ("Tartiblash", {"fields": ("order",)}),
    )


@admin.register(CareerCompany)
class CareerCompanyAdmin(ModelAdmin):
    list_display = ('name', 'career_path', 'logo_preview')
    search_fields = ('name',)

    @admin.display(description="Logo")
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="40" height="30" style="object-fit:contain;">', obj.logo.url)
        return "—"
