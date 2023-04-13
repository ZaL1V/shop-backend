from rest_framework import serializers
from .models import Items


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['article', 'title', 'category', 'price', 'discount_price', 'sex', 'size', 'shop', 'image']
