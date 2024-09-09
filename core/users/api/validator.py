from core.users.api.exceptions import SenhasNaoCoincidemError


def validar_senhas_coincidem(senha, confirmacao_senha):
    """
    Validador personalizado para verificar se as senhas coincidem.

    Parâmetros:
        senha (str): A senha fornecida.
        confirmacao_senha (str): A confirmação da senha fornecida.

    Levanta:
        SenhasNaoCoincidemError: Se as senhas não coincidirem.
    """
    if senha != confirmacao_senha:
        raise SenhasNaoCoincidemError
