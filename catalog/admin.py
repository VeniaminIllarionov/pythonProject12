from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('id',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version', 'number_version', 'current_version')
    list_filter = ('product',)
    search_fields = ('version',)