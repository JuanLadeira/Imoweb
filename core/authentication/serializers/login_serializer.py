from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    """
    Subclasse de TokenObtainPairSerializer para customização do processo de obtenção de tokens.

    Esta classe estende a funcionalidade padrão do TokenObtainPairSerializer para incluir
    informações adicionais no token JWT, como o tipo de usuário e um identificador específico
    do usuário baseado em seu tipo. Ela também personaliza a validação de autenticação para
    tratar casos específicos de erro.

    Métodos:
        get_token: Gera um token JWT customizado com informações adicionais.
        validate: Valida as credenciais do usuário e gera o token JWT.
    """

    mensagens_padroes_de_erro = {
        "contao_nao_ativa": _("Credenciais inválidas."),
    }

    @classmethod
    def get_token(cls, user):
        """
        Gera um token JWT customizado para o usuário.

        Este método adiciona informações adicionais ao token, como o tipo de usuário e
        um identificador específico, além de definir o tempo de expiração do token.

        Parâmetros:
            user (User): O usuário para o qual o token será gerado.

        Retorna:
            Token: Um token JWT customizado.
        """

        token = super().get_token(user)

        token["tipo"] = user.tipo
        if user.tipo == "inquilino":
            token["id_especifico"] = user.inquilino.id
        elif user.tipo == "agente":
            token["id_especifico"] = user.agente.id
        elif user.tipo == "proprietario":
            token["id_especifico"] = user.proprietario.id
        else:
            raise AuthenticationFailed
        return token

    def validate(self, attrs):
        """
        Este medodo valida as credenciais de usuario e verifica se o usuario esta ativo.

        Parâmetros:
            attrs (dict): Atributos contendo o nome de usuário e senha.

        Levanta:
            AuthenticationFailed: Se a autenticação falhar.
        """
        self.user = authenticate(
            request=self.context.get("request"),
            username=attrs.get("username"),
            password=attrs.get("password"),
        )

        if self.user is None or not self.user.is_active:
            raise AuthenticationFailed(
                self.mensagens_padroes_de_erro["contao_nao_ativa"]
            )

        return super().validate(attrs)
