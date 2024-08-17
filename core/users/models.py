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
    contato = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email


class Proprietario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.__str__()


class AgenteImobiliario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.__str__()


class Inquilino(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.__str__()
