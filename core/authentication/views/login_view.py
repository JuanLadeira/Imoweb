from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from core.authentication.serializers.login_serializer import LoginSerializer
from core.authentication.serializers.login_serializer import ResponseLoginSerializer


@extend_schema(
    tags=["Auth"],
    summary="Auth - Login View",
    description="Este endpoint valida as credenciais do usuário e, se forem válidas, retorna um token de acesso e um token de refresh.",
    request=LoginSerializer,
    responses={
        200: ResponseLoginSerializer,
        400: OpenApiResponse(description="Erro de autenticação."),
    },
    parameters=[
        OpenApiParameter(
            name="username",
            description="Nome de usuário",
            type=str,
            required=True,
        ),
        OpenApiParameter(
            name="password",
            description="Senha do usuário",
            type=str,
            required=True,
        ),
    ],
    examples=[
        OpenApiExample(
            name="Exemplo de Token Request",
            description="Exemplo de uma requisição válida para obter tokens de acesso e refresh. A requisição deve incluir o nome de usuário e a senha.",
            value={"username": "usuario", "password": "senha123"},
            request_only=True,
        ),
    ],
)
class LoginView(TokenObtainPairView):
    """'
    View personalizada para a obtenção de pares de tokens JWT (JSON Web Tokens).

    Utiliza 'LoginSerializer' para validar as credenciais do usuário e,
    se bem-sucedido, retorna um 'access' e um 'refresh' token.

    - **Parâmetros**:
      - `username`: Nome de usuário.
      - `password`: Senha do usuário.

    - **Respostas**:
      - `200`: Retorna os tokens 'access' e 'refresh' se as credenciais forem válidas.
      - `400`: Retorna uma mensagem de erro se as credenciais forem inválidas.
    """

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
