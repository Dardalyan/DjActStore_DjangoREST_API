from rest_framework import serializers

from model.user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'phone','dial_code','country_code','is_active', 'is_staff', 'is_superuser', 'last_login']



