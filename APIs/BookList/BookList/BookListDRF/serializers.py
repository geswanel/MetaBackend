from rest_framework import serializers
from .models import Book, Genre
from decimal import Decimal

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre']

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    #author = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    inventory = serializers.IntegerField()
    genre = GenreSerializer()

class BookModelSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    tax_price = serializers.SerializerMethodField(method_name='full_price')
    genre = serializers.StringRelatedField()    # if commented only id
    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'stock', 'genre', 'tax_price']
    
    def full_price(self, book: Book):
        return book.price * Decimal(1.1)