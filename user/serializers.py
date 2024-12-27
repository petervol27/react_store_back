from rest_framework import serializers
from .models import ShopUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom claims
        data["is_admin"] = self.user.is_staff  # Check if the user is an admin

        return data
