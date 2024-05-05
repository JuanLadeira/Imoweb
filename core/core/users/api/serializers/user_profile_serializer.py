from rest_framework import serializers
from core.users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['contato', 'endereco']
