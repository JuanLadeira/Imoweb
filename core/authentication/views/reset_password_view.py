from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication.serializers.reset_password_serializer import (
    ResetPasswordSerializer,
)
from core.authentication.utils import CustomTokenGenerator

custom_token_generator = CustomTokenGenerator()
User = get_user_model()


@extend_schema(
    tags=["Auth"],
    summary="Auth - Redefine a senha de um usuário.",
    description="Redefine a senha de um usuário.",
    request=ResetPasswordSerializer,
    responses={
        200: {"description": "Senha redefine com sucesso."},
        400: {"description": "Token inválido ou usuário não encontrado."},
    },
    examples=[
        OpenApiExample(
            name="Exemplo 1",
            description="Exemplo de uma requisição válida para redefinir minha senha. A requisição deve incluir o token, email e a new_password.",
            value={
                "token": "abc123",
                "email": "email@example.com",
                "new_password": "nova_senha",
            },
            request_only=True,
        ),
        OpenApiExample(
            name="200 example",
            description="Exemplo de uma resposta válida para redefinir minha senha. A resposta deve incluir a mensagem.",
            value={
                "message": "Senha redefinida com sucesso.",
            },
            response_only=True,
        ),
        OpenApiExample(
            name="400 example",
            description="Exemplo de uma resposta inválida para redefinir minha senha. A resposta deve incluir a mensagem.",
            value={
                "message": "Token inválido ou usuário não encontrado.",
            },
            response_only=True,
        ),
    ],
)
class ResetPasswordView(APIView):
    """
    View para redefinir a senha de um usuário utilizando um token de redefinição.

    Esta view permite ao usuário redefinir sua senha fornecendo um token válido, seu email e a nova senha desejada.
    O processo verifica se o token corresponde ao usuário e, em caso afirmativo, atualiza a senha do usuário.

    Métodos:
        post(request): Recebe o token, email e nova senha do usuário, redefinindo a senha se o token for válido.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        """
        View para redefinir a senha de um usuário utilizando um token de redefinição.

        Esta view permite ao usuário redefinir sua senha fornecendo um token válido, seu email e a nova senha desejada.
        O processo verifica se o token corresponde ao usuário e, em caso afirmativo, atualiza a senha do usuário.

        Métodos:
            post(request): Recebe o token, email e nova senha do usuário, redefinindo a senha se o token for válido.
        """

        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data["token"]
        email = serializer.validated_data["email"]
        new_password = serializer.validated_data["new_password"]

        user = User.objects.filter(email=email).first()
        if user and custom_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({"message": "Senha redefinida com sucesso."})
        return Response(
            {"message": "Token inválido ou usuário não encontrado."},
            status=400,
        )
