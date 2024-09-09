from datetime import timedelta

from django.contrib.auth.tokens import PasswordResetTokenGenerator


class CustomTokenGenerator(PasswordResetTokenGenerator):
    """
    Gerador de token personalizado para redefinição de senha, estendendo o PasswordResetTokenGenerator do Django.

    Esta classe personaliza o processo de geração de tokens para redefinição de senha, permitindo
    a definição de um tempo de vida específico para o token e a inclusão de informações adicionais
    no hash do token, como o ID do usuário e a senha atual.

    Métodos:
        _make_hash_value: Gera um valor de hash único para o token, incluindo o ID do usuário,
                          a marca de tempo e a senha atual do usuário.

    Propriedades:
        password_reset_timeout_days: Define o tempo de vida do token para redefinição de senha.
    """

    def _make_hash_value(self, user, timestamp) -> str:
        """
        Gera um valor de hash que será usado para criar o token de redefinição de senha.

        Este método personaliza o valor de hash incluindo o ID do usuário, a marca de tempo
        e a senha atual do usuário, garantindo que o token seja único e seguro.

        Parâmetros:
            user (User): O usuário para o qual o token de redefinição de senha está sendo gerado.
            timestamp (int): A marca de tempo usada para garantir a unicidade do token.

        Retorna:
            str: Um valor de hash único baseado no usuário e na marca de tempo.
        """

        return str(user.pk) + str(timestamp) + str(user.password)

    @property
    def password_reset_timeout_days(self):
        """
        Define o tempo de vida do token de redefinição de senha.

        Esta propriedade personaliza o tempo de vida do token para 15 minutos, diferentemente
        do padrão do Django, proporcionando uma janela de tempo mais curta para maior segurança.

        Retorna:
            timedelta: O tempo de vida do token, definido para 15 minutos.
        """
        return timedelta(
            minutes=15,
        )
