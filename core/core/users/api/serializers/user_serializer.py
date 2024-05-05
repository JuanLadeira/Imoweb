from rest_framework import serializers
from core.users.models import User, UserProfile
from core.users.api.serializers.user_profile_serializer import UserProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)  # Permitir criação de usuário sem perfil

    class Meta:
        model = User
        fields = ["username", "name", "url", "user_type", "profile"]
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create_user(**validated_data)
        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        return user
