from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    list_filter = ["manufacturer__name"]
    search_fields = ["model"]


@admin.register(Driver)
class Driver(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


admin.site.register(Manufacturer)