from rest_framework import serializers

from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['slug', 'variant_name', ]


class BaseProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.BaseProduct
        fields = ['slug', 'name', 'description', 'price', 'image', 'products']


class CategorySerializer(serializers.ModelSerializer):
    base_products = BaseProductSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = ['slug', 'name', 'base_products']
