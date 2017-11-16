# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Product, Variant, Item

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}
    inlines = [ItemInline, ]
    exclude = ('variants',)


class VariantAdmin(admin.ModelAdmin):
    inlines = [ItemInline, ]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Item)
