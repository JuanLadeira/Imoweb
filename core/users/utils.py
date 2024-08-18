def get_especific_user_data(validated_data: dict) -> tuple[dict, dict]:
    """
    Extracts the user data from the validated data and returns it as a tuple
    with the user data and the remaining data.

    Extrai os dados do usuário dos dados validados e retorna-os como uma tupla
    com os dados do usuário e os dados restantes.
    """
    usuario_data = {}

    usuario_fields = [
        "username",
        "password",
        "password2",
        "first_name",
        "last_name",
        "tipo",
        "telefone",
        "email",
        "foto",
        "endereco",
    ]

    for field in usuario_fields:
        if field in validated_data:
            usuario_data[field] = validated_data.pop(field)

    return usuario_data, validated_data
