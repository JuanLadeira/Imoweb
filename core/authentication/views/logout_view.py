from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from core.authentication.serializers.logout_serializer import LogoutSerializer


@extend_schema(
    tags=["Auth"],
    summary="Auth - Logout View",
    description="Use este endpoint para deslogar usuários invalidando o refresh token fornecido.",
    parameters=[
        OpenApiParameter(
            name="refresh_token",
            required=True,
            type=str,
            location=OpenApiParameter.QUERY,
            description="Refresh token a ser invalidado",
        ),
    ],
    request=LogoutSerializer,
    responses={
        205: OpenApiResponse(
            description="Logout bem-sucedido, refresh token foi invalidado.",
        ),
        400: OpenApiResponse(
            description="Falha no pedido, possivelmente devido à ausência do refresh token.",
        ),
    },
)
@api_view(["POST"])
@permission_classes(
    [IsAuthenticated],
)
def logout_view(request):
    """
    Endpoint de Logout

    Use este endpoint para deslogar usuários invalidando o refresh token fornecido.

    **Parâmetros**

    - `refresh_token`: Um string contendo o refresh token que será invalidado.

    **Corpo da Requisição**

    ```
    {
        "refresh_token": "<refresh_token>"
    }
    ```

    **Respostas**

    - `205 Reset Content`: Logout bem-sucedido, refresh token foi invalidado.
    - `400 Bad Request`: Falha no pedido, possivelmente devido à ausência do refresh token.

    **Exemplo de Pedido**

    POST /api/logout
    Content-Type: application/json

    {
        "refresh_token": "eyddd11415413#!..."
    }

    """
    refresh_token = request.data.get("refresh_token")

    if refresh_token is None:
        return Response(
            {"error": "Refresh token is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response(
        {"detail": "Logout realizado com sucesso."},
        status=status.HTTP_205_RESET_CONTENT,
    )
