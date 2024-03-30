from rest_framework import serializers
from . import models
from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'category_name']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    #category = CategorySerializer()
    category = serializers.HyperlinkedRelatedField(
        queryset = models.Category.objects.all(),
        view_name='category-detail',
    )
    price_after_tax = serializers.SerializerMethodField(method_name='tax_price')
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'stock', 'category', 'price_after_tax']
        #depth = 1
    
    @staticmethod
    def tax_price(item):
        return item.price * Decimal(1.01)


class MenuItemFuncSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'category', 'category_id']


class HyperlinkedMenuItemSerializer(serializers.HyperlinkedModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    #category = CategorySerializer()
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = models.Category.objects.all(),
    #     view_name='category-detail'
    # )
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'category']
        #depth = 1