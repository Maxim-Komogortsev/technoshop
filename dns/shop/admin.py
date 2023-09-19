from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'description', 'stock', 'available', 'created', 'update']
    list_filter = ['update', 'available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {
        'slug': ('name', )
    }


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name', )
    }


admin.site.register(Category, CategoryAdmin)
