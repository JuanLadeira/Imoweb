from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for core.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    USER_TYPE_CHOICES = (
        ("proprietario", "Proprietário"),
        ("agente", "Agente Imobiliário"),
        ("inquilino", "Inquilino"),
    )
    tipo = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default="proprietario",
    )
    endereco = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255, blank=True)
    foto = models.ImageField(upload_to="fotos/", null=True, blank=True)

    def __str__(self):
        return self.email


class Proprietario(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="proprietario"
    )

    def __str__(self) -> str:
        return f"Proprietario {self.user.__str__()}"


class AgenteImobiliario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agente")

    def __str__(self) -> str:
        return f"Agente {self.user.__str__()}"


class Inquilino(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="inquilino"
    )

    def __str__(self) -> str:
        return f"Inquilino {self.user.__str__()}"
