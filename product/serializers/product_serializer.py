from rest_framework import serializers

from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'active',
            'categories',
            'categories_id',
        ]

    def create(self, validated_data):
        category_data = validated_data.pop('categories_id')

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.categories.add(category)
            
        return product