from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.users.models import User, UserProfile
from core.users.api.serializers.user_profile_serializer import UserProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)  # Permitir criação de usuário sem perfil

    class Meta:
        model = User
        fields = ["username", "name", "user_type", "profile"]

    @transaction.atomic
    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create_user(**validated_data)
        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        if profile_data:
            profile, created = UserProfile.objects.get_or_create(user=instance)
            profile_serializer = UserProfileSerializer(profile, data=profile_data, partial=True)
            if profile_serializer.is_valid(raise_exception=True):
                profile_serializer.save()

        return super().update(instance, validated_data)