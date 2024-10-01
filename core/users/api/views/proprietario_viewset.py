from logging import getLogger

from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from core.users.api.serializers.proprietario_serializer import ProprietarioGetSerializer
from core.users.api.serializers.proprietario_serializer import (
    ProprietarioPostSerializer,
)
from core.users.api.serializers.proprietario_serializer import (
    ProprietarioUpdateSerializer,
)
from core.users.models import Proprietario

logger = getLogger("django")


@extend_schema(tags=["Proprietários"])
class ProprietarioViewSet(viewsets.ModelViewSet):
    """
    Endpoint de Proprietários
    """

    queryset = Proprietario.objects.all()
    item_name = "Proprietário"
    plural_item_name = "Proprietários"
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_proprietario:
            return self.queryset.filter(user=user)
        if user.is_agente:
            return self.queryset.all()
        return self.queryset.none()

    def get_serializer_class(self):
        if self.request.method in {"GET"}:
            return ProprietarioGetSerializer
        if self.request.method in {"PUT", "PATCH"}:
            return ProprietarioUpdateSerializer
        return ProprietarioPostSerializer

    @extend_schema(
        summary=f"Lista todos os {item_name}s",
        description=f"""
        Este endpoint lista todos os {item_name}s.
        Retorna uma lista paginada de {item_name}s
        """,
        responses={
            200: ProprietarioGetSerializer(many=True),
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary=f"Cria um novo {item_name}",
        description=f"Este endpoint permite criar um novo {item_name}.",
        request=ProprietarioPostSerializer,
        responses={
            201: ProprietarioGetSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary=f"Recupera um {item_name}",
        description=f"Este endpoint permite recuperar um {item_name} específico.",
        responses={
            200: ProprietarioGetSerializer,
            404: OpenApiResponse(description=f"{item_name} não encontrado"),
        },
    )
    def retrieve(self, request, slug=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @extend_schema(
        summary=f"Atualiza um {item_name}",
        description=f"Este endpoint permite atualizar um {item_name} específico.",
        request=ProprietarioPostSerializer,
        responses={
            200: ProprietarioGetSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary=f"Atualiza parcialmente um {item_name}",
        description=f"""
        Este endpoint permite atualizar
        parcialmente um {item_name} específico.
        """,
        request=ProprietarioPostSerializer,
        responses={
            200: ProprietarioGetSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary=f"Exclui um {item_name}",
        description=f"Este endpoint permite excluir um {item_name} específico.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
