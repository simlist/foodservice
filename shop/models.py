# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class BaseProduct(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='product images/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    base_product = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=20)
    price_added = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      default=0.00)
    group_name = models.CharField(max_length=20)

    def __str__(self):
        return ' - '.join((self.base_product.name, self.variant_name))

    @property
    def price(self):
        return self.base_product.price + self.price_added

