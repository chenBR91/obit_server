from rest_framework import serializers

from .models import Category, Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "description",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
        )


class CategorySerializers(serializers.ModelSerializer):
    products = ProductSerializers(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )