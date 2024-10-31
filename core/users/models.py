from django.contrib.auth.models import AbstractUser
from django.db import models


class UserType(models.TextChoices):
    """
    Enumeração que representa os diferentes tipos de usuário no sistema.

    Os tipos de usuário incluem:
    - PROPRIETARIO: Representa um proprietário.
    - AGENTE: Representa um agente imobiliário.
    - INQUILINO: Representa um inquilino.

    Attributes:
        value (str): O valor interno do enum usado para armazenar a escolha.
        display_name (str): O nome legível associado ao valor do enum, que será exibido para os usuários.

    Methods:
        choices():
            Retorna uma lista de tuplas (valor, nome legível) para uso em campos de escolha de modelos Django.
             Examples:
        # Criação de um valor específico do enum
    user_type = UserType.PROPRIETARIO
    print(user_type.value)         # Output: "proprietario"
    print(user_type.display_name)  # Output: "Proprietário"


    """

    PROPRIETARIO = "proprietario", "Proprietário"
    AGENTE = "agente", "Agente Imobiliário"
    INQUILINO = "inquilino", "Inquilino"


class User(AbstractUser):
    """
    Default custom user model for core.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    tipo = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.PROPRIETARIO.value,
    )
    endereco = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255, blank=True)
    foto = models.ImageField(upload_to="fotos/", null=True, blank=True)

    def __str__(self):
        return self.get_full_name() or self.username

    def get_tipo_display_name(self) -> str:
        """
        Obtém o nome legível associado ao valor do campo `tipo`.

        Percorre os valores do enum `UserType` para encontrar o nome legível
        correspondente ao valor armazenado no campo `tipo`.

        Returns:
            str: O nome legível do tipo de usuário. Retorna "Tipo desconhecido" se o valor não for encontrado.
        """
        matching_types = [
            user_type.label for user_type in UserType if user_type.value == self.tipo
        ]
        return matching_types[0] if matching_types else "Tipo desconhecido"

    @property
    def is_proprietario(self) -> bool:
        """
        Verifica se o usuário é um proprietário.

        Returns:
            bool: True se o usuário for um proprietário, False caso contrário.
        """
        return self.tipo == UserType.PROPRIETARIO.value

    @property
    def is_agente(self) -> bool:
        """
        Verifica se o usuário é um agente imobiliário.

        Returns:
            bool: True se o usuário for um agente imobiliário, False caso contrário.
        """
        return self.tipo == UserType.AGENTE.value

    @property
    def is_inquilino(self) -> bool:
        """
        Verifica se o usuário é um inquilino.

        Returns:
            bool: True se o usuário for um inquilino, False caso contrário.
        """
        return self.tipo == UserType.INQUILINO.value


class Proprietario(models.Model):
    """
    Modelo que representa um proprietário no sistema.

    Este modelo é usado para armazenar informações adicionais sobre usuários
    que são identificados como proprietários. O relacionamento com o modelo `User`
    é estabelecido por meio de uma relação de um-para-um.

    Attributes:
        user (OneToOneField): Referência ao modelo `User`. Cada instância de `Proprietario`
        está associada a um único usuário. A relação é estabelecida usando a chave
        estrangeira que é excluída em cascata quando o usuário associado é excluído.

    Example:
        # Criação de um proprietário e associando um usuário a ele
        user = User.objects.create_user(username="username", password="password")
        proprietario = Proprietario.objects.create(user=user)
        print(proprietario)  # Output: Proprietario example@example.com
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name=UserType.PROPRIETARIO.value,
        primary_key=True,
    )

    def __str__(self) -> str:
        return f"{self.user.__str__()}"

    @property
    def id(self):
        return self.user.id


class AgenteImobiliario(models.Model):
    """
    Modelo que representa um agente imobiliário no sistema.

    Este modelo é usado para armazenar informações adicionais sobre usuários
    que são identificados como agentes imobiliários. O relacionamento com o modelo `User`
    é estabelecido por meio de uma relação de um-para-um.

    Attributes:
        user (OneToOneField): Referência ao modelo `User`. Cada instância de `AgenteImobiliario`
        está associada a um único usuário. A relação é estabelecida usando a chave
        estrangeira que é excluída em cascata quando o usuário associado é excluído.

    Methods:
        __str__():
            Retorna uma representação legível para o agente imobiliário, que inclui o email
            do usuário associado, precedido pela string "Agente".

    Example:
        # Criação de um agente imobiliário e associando um usuário a ele
        user = User.objects.create_user(username="username", password="password")
        agente = AgenteImobiliario.objects.create(user=user)
        print(agente)  # Output: Agente example@example.com
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name=UserType.AGENTE.value,
        primary_key=True,
    )

    def __str__(self) -> str:
        return f"{self.user.__str__()}"

    @property
    def id(self):
        return self.user.id


class Inquilino(models.Model):
    """
    Modelo que representa um inquilino no sistema.

    Este modelo é usado para armazenar informações adicionais sobre usuários
    que são identificados como inquilinos. O relacionamento com o modelo `User`
    é estabelecido por meio de uma relação de um-para-um.

    Attributes:
        user (OneToOneField): Referência ao modelo `User`. Cada instância de `Inquilino`
        está associada a um único usuário. A relação é estabelecida usando a chave
        estrangeira que é excluída em cascata quando o usuário associado é excluído.

    Methods:
        __str__():
            Retorna uma representação legível para o inquilino, que inclui o email
            do usuário associado, precedido pela string "Inquilino".

    Example:
        # Criação de um inquilino e associando um usuário a ele
        user = User.objects.create_user(username="username", password="password")
        inquilino = Inquilino.objects.create(user=user)
        print(inquilino)  # Output: Inquilino example@example.com
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name=UserType.INQUILINO.value,
        primary_key=True,
    )

    def __str__(self) -> str:
        return f"{self.user.__str__()}"

    @property
    def id(self):
        return self.user.id
