from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from core.propriedade.api.serializers.tipo_de_imovel_serializer import (
    TipoDeImovelGetSerializer,
)
from core.propriedade.api.serializers.tipo_de_imovel_serializer import (
    TipoDeImovelPostSerializer,
)
from core.propriedade.models import TipoDeImovel


@extend_schema(tags=["Tipos de Imóveis"])
class TipoDeImovelViewSet(viewsets.ModelViewSet):
    queryset = TipoDeImovel.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    item_name = "Tipo de Imovel"
    plural_item_name = "Tipo de imóveis"

    def get_serializer_class(self):
        if self.request.method in {"GET"}:
            return TipoDeImovelGetSerializer
        return TipoDeImovelPostSerializer

    @extend_schema(
        summary=f"Lista todos os {item_name}s",
        description=f"""
        Este endpoint lista todos os {item_name}s.
        Retorna uma lista paginada de {item_name}s
        """,
        responses={
            200: TipoDeImovelGetSerializer(many=True),
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary=f"Recupera um {item_name}",
        description=f"Este endpoint permite recuperar um {item_name} específico.",
        responses={
            200: TipoDeImovelGetSerializer,
            404: OpenApiResponse(description=f"{item_name} não encontrado"),
        },
    )
    def retrieve(self, request, slug=None, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary=f"Cria um novo {item_name}",
        description=f"""
        Este endpoint permite criar um novo {item_name}.
        """,
        request=TipoDeImovelPostSerializer,
        responses={
            201: TipoDeImovelPostSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary=f"Atualiza um {item_name}",
        description=f"Este endpoint permite atualizar um {item_name} específico.",
        request=TipoDeImovelPostSerializer,
        responses={
            200: TipoDeImovelPostSerializer,
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
        request=TipoDeImovelPostSerializer,
        responses={
            200: TipoDeImovelPostSerializer,
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
