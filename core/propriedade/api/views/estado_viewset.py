from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from config.views import CreateUpdateDestroyViewSet
from core.propriedade.api.serializers.estado_serializer import EstadoPostSerializer
from core.propriedade.models import Estado


class EstadoViewSet(CreateUpdateDestroyViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = EstadoPostSerializer
    queryset = Estado.objects.all()

    item_name = "Estado"
    plural_item_name = "Estados"

    @extend_schema(
        summary=f"Cria um novo {item_name}",
        description=f"""
        Este endpoint permite criar um novo {item_name}.
        """,
        request=EstadoPostSerializer,
        responses={
            201: EstadoPostSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary=f"Atualiza um {item_name}",
        description=f"Este endpoint permite atualizar um {item_name} específico.",
        request=EstadoPostSerializer,
        responses={
            200: EstadoPostSerializer,
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
        request=EstadoPostSerializer,
        responses={
            200: EstadoPostSerializer,
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
