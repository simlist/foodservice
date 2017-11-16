# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Product, Variant, Item

class VariantInline(admin.TabularInline):
    model = Product.variants.through
    extra = 2


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}
    inlines = [VariantInline, ]
    exclude = ('variants',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant)
admin.site.register(Item)
