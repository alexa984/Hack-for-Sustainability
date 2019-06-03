from django.contrib import admin
from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'unit_price',
        'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['unit_price', 'available']
    prepopulated_fields = {'slug': ('name',)}