from django.contrib import admin

from . import models


# admin.site.register(models.Animal)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "is_auto_generated",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "city",
        "is_auto_generated",
        "created_at",
    )


class ContactInline(admin.TabularInline):
    model = models.Contact


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "modified_at",
    )
    inlines = (ContactInline,)
