from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductTag, ProductModel, Category, SizeModel, ColorModel, BrandModel
from .forms import ColorForms

from modeltranslation.admin import TranslationAdmin


@admin.register(ProductTag)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'color']
    list_display_links = ['code']
    search_fields = ['code']
    form = ColorForms

    def color(self, obj):
        free_space = '&nbsp;' * 5
        return mark_safe(f"<div style='background-color:{obj.code}; width:200px;'>{free_space}</div>")


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class ProductModelAdmin(TranslationAdmin):
    list_display = ['title', 'price', 'real_price', 'discount', 'created_at', 'sale']
    list_display_links = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'price']
    autocomplete_fields = ['category', 'tags', 'sizes', 'colors']
    readonly_fields = ['real_price', 'sale']

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(ProductModel, ProductModelAdmin)