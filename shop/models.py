# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30)


class ProductVariant(models.Model):
    name = models.CharField(max_length=20)
    group_name = models.CharField(max_length=20)
    price_added = models.DecimalField(max_digits=4, decimal_places=2)


class Product(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=40)
    desription = models.TextField()
    baseprice = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField()
    category = models.ForeignKey(Category)
    variant = models.ManyToManyField(ProductVariant)



