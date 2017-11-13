# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    def natural_key(self):
        return (self.name,)


class ProductVariant(models.Model):
    name = models.CharField(max_length=20)
    group_name = models.CharField(max_length=20)
    price_added = models.DecimalField(max_digits=4, decimal_places=2)

    def natural_key(self):
        return (self.group_name, self.name, self.price_added)


class Product(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField()
    category = models.ForeignKey(Category)
    variant = models.ManyToManyField(ProductVariant)



