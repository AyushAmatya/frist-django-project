from rest_framework import serializers
from EcommerceApp.models import Customers, Items

class CustomerSerializers (serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('CustomerId', 'CustomerName')

class ItemsSerializers (serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('ItemId', 'ItemName', 'ItemInStock')