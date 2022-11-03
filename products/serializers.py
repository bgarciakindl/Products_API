from rest_framework import serializers
from . import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','description','price','inventory_quantity']