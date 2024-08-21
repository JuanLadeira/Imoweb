from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication.serializers.forgot_password_serializer import (
    ForgotPasswordSerializer,
)
from core.authentication.tasks import send_reset_password_email
from core.authentication.utils import CustomTokenGenerator

custom_token_generator = CustomTokenGenerator()
User = get_user_model()


@extend_schema(
    tags=["Auth"],
    summary="Auth - Forgot my password - Envio de Token para redefinição de senha",
    description="Envia um email para o usuário com um token de redefinição de senha.",
    request=ForgotPasswordSerializer,
    responses={
        200: {
            "description": "Se o email fornecido estiver em nossa base de dados, nós enviaremos um email de redefinição de senha.",
        },
    },
    examples=[
        OpenApiExample(
            name="Exemplo de requisição",
            description="Exemplo de uma requisição válida para esqueci minha senha. A requisição deve incluir o email.",
            value={"email": "email@example.com"},
            request_only=True,
        ),
        OpenApiExample(
            name="Exemplo de resposta",
            description="Exemplo de uma resposta válida para esqueci minha senha. A resposta deve incluir a mensagem.",
            value={
                "message": "Se o email fornecido estiver em nossa base de dados, nós enviaremos um email com token para redefinição de senha.",
            },
            response_only=True,
        ),
    ],
)
class ForgotPasswordView(APIView):
    """
    View para solicitar redefinição de senha de um usuário através do envio de um token de redefinição para o email fornecido.

    Esta view trata a solicitação de redefinição de senha, verificando se o email fornecido está associado a um usuário
    e, em caso afirmativo, gera um token de redefinição de senha que é enviado para o email do usuário.

    Métodos:
        post(request): Recebe uma solicitação com o email do usuário e envia um email com o token de redefinição de senha,
                       caso o email esteja associado a um usuário cadastrado.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        """
        Trata a solicitação POST para iniciar o processo de redefinição de senha.

        Verifica se o email fornecido está associado a um usuário. Se estiver, gera um token de redefinição de senha
        e envia esse token para o email do usuário.

        Parâmetros:
            request (Request): A solicitação HTTP.

        Retorna:
            Response: Uma resposta HTTP indicando se o email de redefinição de senha foi enviado.
        """
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        user = User.objects.filter(email=email).first()
        if user:
            token = custom_token_generator.make_token(user)
            send_reset_password_email.delay(email, token)

        return Response(
            {
                "message": "Se o email fornecido estiver em nossa base de dados, nós enviaremos um email de redefinição de senha.",
            },
        )
