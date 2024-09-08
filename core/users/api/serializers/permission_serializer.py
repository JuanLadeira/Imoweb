from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    """
    A classe PermissionSerializer é responsável por serializar os dados de uma permissão.
    """

    codename = serializers.CharField()

    class Meta:
        model = Permission
        fields = ["codename"]
