from logging import getLogger

from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenVerifyView

logger = getLogger("django")


@extend_schema(
    tags=["Auth"],
    summary="Auth - Verificar Token (VERIFY)",
    description="Este endpoint permite que um usuário verifique a validade de um access token.",
    responses={
        200: {"description": "O token é válido"},
        401: {"description": "Token inválido ou expirado"},
    },
    examples=[
        OpenApiExample(
            name="Exemplo de Verify Token Request",
            summary="Exemplo de Verify Token Request",
            description="Requisição para verificar a validade do access token.",
            value={"token": "<seu_access_token_aqui>"},
            response_only=True,
        ),
    ],
)
class VerifyTokenView(TokenVerifyView):
    """
    Uma view personalizada para verificar a validade de tokens de acesso JWT.

    Esta classe estende `TokenVerifyView` do `rest_framework_simplejwt.views`, adicionando documentação específica
    para o endpoint de verificação de token através do decorador `@extend_schema`.

    O objetivo é fornecer informações detalhadas sobre o endpoint para a documentação da API,
    incluindo tags, um resumo, descrição, possíveis respostas
    HTTP e exemplos de requisição.

    Atributos:
        throttle_classes (list): Uma lista de classes de controle de acesso (throttling) aplicadas a esta view.
                                 Por padrão, está vazia, indicando que não há controle de acesso por throttling.

    Métodos herdados:
        post(request, *args, **kwargs): Recebe uma requisição POST com um token JWT e verifica sua validade.
                                        Retorna uma resposta HTTP indicando se o token é válido ou não.

    Exemplos de uso e respostas esperadas são fornecidos na documentação estendida através do decorador `@extend_schema`.
    """

    throttle_classes = []
