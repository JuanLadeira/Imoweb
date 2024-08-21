from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenRefreshView


@extend_schema(
    tags=["Auth"],
    summary="Auth - Refresh Token",
    description="Este endpoint permite que um usuário renove seu access token usando um refresh token.",
    responses={
        200: {"description": "Novo access token gerado"},
        400: {"description": "Refresh token inválido ou expirado"},
    },
    examples=[
        OpenApiExample(
            name="Exemplo de Refresh Token Request",
            summary="Exemplo de Refresh Token Request",
            description="Requisição válida para obter um novo access token usando um refresh token.",
            value={"refresh": "<seu_refresh_token_aqui>"},
            response_only=True,
        ),
    ],
)
class RefreshTokenView(TokenRefreshView):
    """
    View para renovar o access token usando o refresh token.

    - **Parâmetros**:
      - `refresh`: O refresh token que será usado para gerar um novo access token.

    - **Respostas**:
      - `200`: Retorna um novo access token se o refresh token for válido.
      - `400`: Retorna uma mensagem de erro se o refresh token for inválido ou estiver expirado.
    """
