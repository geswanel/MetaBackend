from rest_framework import serializers
from .models import Category, MenuItem
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    category = CategorySerializer(read_only=True)
    category_id =  serializers.IntegerField(write_only=True)
    price_after_tax = serializers.SerializerMethodField(method_name='tax_price')
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'price_after_tax', 'stock', 'category', 'category_id']
    
    @staticmethod
    def tax_price(item):
        return item.price * Decimal(1.1)