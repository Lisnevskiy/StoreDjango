from django.contrib import admin

from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'publishing_flag',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'publishing_flag', 'views_count',)
    search_fields = ('title',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'current_version', 'product',)
    search_fields = ('product',)
