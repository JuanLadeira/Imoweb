from logging import getLogger

from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioGetSerializer,
)
from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioPostSerializer,
)
from core.users.models import AgenteImobiliario

logger = getLogger("django")


@extend_schema(tags=["Agente Imobiliario"])
class AgenteImobiliarioViewSet(viewsets.ModelViewSet):
    """
    Endpoint de Agente Imobiliario
    """

    queryset = AgenteImobiliario.objects.all()
    item_name = "Agente Imobiliario"
    plural_item_name = "Agentes imobiliarios"
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
    ]

    def get_queryset(self):
        user = self.request.user
        query = self.queryset.all()
        if user.is_agente:
            return query
        return query.none()

    def get_serializer_class(self):
        if self.request.method in ["GET"]:
            return AgenteImobiliarioGetSerializer
        return AgenteImobiliarioPostSerializer

    @extend_schema(
        summary=f"Lista todos os {item_name}s",
        description=f"""
        Este endpoint lista todos os {item_name}s.
        Retorna uma lista paginada de {item_name}s
        """,
        responses={
            200: AgenteImobiliarioGetSerializer(many=True),
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def list(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_inquilino:
            raise PermissionDenied

        if user.is_proprietario:
            raise PermissionDenied

        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary=f"Cria um novo {item_name}",
        description=f"""
        Este endpoint permite criar um novo {item_name}.
        """,
        request=AgenteImobiliarioPostSerializer,
        responses={
            201: AgenteImobiliarioGetSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary=f"Recupera um {item_name}",
        description=f"Este endpoint permite recuperar um {item_name} específico.",
        responses={
            200: AgenteImobiliarioGetSerializer,
            404: OpenApiResponse(description=f"{item_name} não encontrado"),
        },
    )
    def retrieve(self, request, slug=None, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary=f"Atualiza um {item_name}",
        description=f"Este endpoint permite atualizar um {item_name} específico.",
        request=AgenteImobiliarioPostSerializer,
        responses={
            200: AgenteImobiliarioGetSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary=f"Atualiza parcialmente um {item_name}",
        description=f"""
        Este endpoint permite atualizar parcialmente um {item_name} específico.
        """,
        request=AgenteImobiliarioPostSerializer,
        responses={
            200: AgenteImobiliarioGetSerializer,
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
