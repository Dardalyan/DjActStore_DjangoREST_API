from rest_framework import serializers

from model.order.models import Order
from serializers.productSerializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


