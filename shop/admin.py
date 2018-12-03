# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, BaseProduct, Product

class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}

class BaseProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',]}
    inlines = [ProductInline,]

class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug', )

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BaseProduct, BaseProductAdmin)
