from rest_framework import serializers

from model.basket.models import Basket
from serializers.productSerializer import ProductSerializer


class BasketSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Basket
        fields = '__all__'
