from rest_framework import serializers
from .models import Address

class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['country', 'city', 'street', 'number']
