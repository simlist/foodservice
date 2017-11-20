# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from .models import Product, Category

def index(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        products = Product.objects.all()
        data = {category.name: products.filter(category__name=category.name) for
                category in categories}
        return render(request, 'shop/index.html', {'products_by_cat': data})

def product(request):
    if request.method == 'GET':
        product = Product.objects.filter(slug=request.GET.get('slug'))
        data = serializers.serialize('json', product)
        return HttpResponse(data, content_type='application/json')
