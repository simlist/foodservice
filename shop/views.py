# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from .models import Product

def index(request):
    data = serializers.serialize('json', Product.objects.all(),
                                 use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')

def product(request):
    if request.method == 'GET':
        product = Product.objects.filter(slug=request.GET.get('slug'))
        data = serializers.serialize('json', product)
        return HttpResponse(data, content_type='application/json')
