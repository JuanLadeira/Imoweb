from logging import getLogger

from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from core.users.api.serializers.inquilino_serializer import (
    InquilinoProfileGetSerializer,
)
from core.users.api.serializers.inquilino_serializer import (
    InquilinoProfilePostSerializer,
)
from core.users.models import InquilinoProfile

logger = getLogger("django")


@extend_schema(tags=["Inquilinos"])
class InquilinoProfileViewSet(viewsets.ModelViewSet):
    """
    Endpoint de Inquilinos
    """

    item_name = "Inquilino"
    plural_item_name = "Inquilinos"
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
    ]

    def get_queryset(self):
        return InquilinoProfile.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["GET"]:
            return InquilinoProfileGetSerializer
        return InquilinoProfilePostSerializer

    @extend_schema(
        summary=f"Lista todos os {item_name}s",
        description=f"""
        Este endpoint lista todos os {item_name}s.
        Retorna uma lista paginada de {item_name}s
        """,
        responses={
            200: InquilinoProfileGetSerializer(many=True),
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary=f"Cria um novo {item_name}",
        description=f"Este endpoint permite criar um novo {item_name}.",
        request=InquilinoProfilePostSerializer,
        responses={
            201: InquilinoProfileGetSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary=f"Recupera um {item_name}",
        description=f"Este endpoint permite recuperar um {item_name} específico.",
        responses={
            200: InquilinoProfileGetSerializer,
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
        request=InquilinoProfilePostSerializer,
        responses={
            200: InquilinoProfileGetSerializer,
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
        request=InquilinoProfilePostSerializer,
        responses={
            200: InquilinoProfileGetSerializer,
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
