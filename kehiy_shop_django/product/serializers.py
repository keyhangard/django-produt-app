from dataclasses import field
from itertools import product
from rest_framework import serializers
from .models import Category,Product

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = product
#         fields = (
#             "id",
#             "name",
#             "get_absolute_url",
#             "description",
#             "price",
#             "get_image",
#             "get_thumbnail"
#         )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )