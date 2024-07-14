from rest_framework import serializers

from model.address.models import Address
#from serializers.userSerializer import UserSerializer


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
