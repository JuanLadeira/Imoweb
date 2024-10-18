from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from config.views import CreateUpdateDestroyViewSet
from core.propriedade.api.serializers.foto_serializer import FotoPostSerializer
from core.propriedade.models import Foto


@extend_schema(tags=["Fotos"])
class FotoViewSet(CreateUpdateDestroyViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = FotoPostSerializer
    queryset = Foto.objects.all()

    item_name = "Foto"
    plural_item_name = "Fotos"

    @extend_schema(
        summary=f"Cria uma nova {item_name}",
        description=f"""
        Este endpoint permite criar uma nova {item_name}.
        """,
        request=FotoPostSerializer,
        responses={
            201: FotoPostSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary=f"Atualiza uma {item_name}",
        description=f"""
        Este endpoint permite atualizar uma {item_name} específica.
        """,
        request=FotoPostSerializer,
        responses={
            200: FotoPostSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary=f"Atualiza parcialmente uma {item_name}",
        description=f"""
        Este endpoint permite atualizar parcialmente uma {item_name} específica.
        """,
        request=FotoPostSerializer,
        responses={
            200: FotoPostSerializer,
            400: OpenApiResponse(description="Erro de validação"),
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary=f"Exclui uma {item_name}",
        description=f"""
        Este endpoint permite excluir uma {item_name} específica.
        """,
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
