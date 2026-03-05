from django.contrib import admin
from .models import Property, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "city", "created_at")
    search_fields = ("title", "city")
    list_filter = ("city", "property_type")


admin.site.register(Property, PropertyAdmin)
admin.site.register(Review)