from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.users.api.serializers.user_logged_in_serializer import UserLoggedInSerializer


@extend_schema(
    tags=["Usuario Autenticado"],
    summary="""
    Usuario Autenticado Endpoint.
""",
    description="""
    Endpoint que retorna dados do usuario que está autenticado na aplicação.
""",
    request=None,
    responses=UserLoggedInSerializer,
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_logged_in_view(request):
    usuario = request.user
    serializer = UserLoggedInSerializer(usuario)
    return Response(serializer.data, status=status.HTTP_200_OK)
