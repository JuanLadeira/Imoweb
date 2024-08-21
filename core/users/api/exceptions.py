from rest_framework import serializers


class SenhasNaoCoincidemError(serializers.ValidationError):
    """
    Exceção personalizada para senhas que não coincidem.

    Esta exceção é levantada quando as senhas fornecidas não coincidem.
    """

    default_detail = "As senhas não coincidem, tente novamente."
    default_code = "senhas_nao_coincidem"
