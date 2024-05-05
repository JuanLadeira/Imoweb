from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for core.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    USER_TYPE_CHOICES = (
        ('cliente', 'Cliente'),
        ('agente', 'Agente Imobiliário'),
        ('inquilino', 'Inquilino'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='cliente')

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contato = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, null=True, blank=True)

class ClienteProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    preferencias_de_busca = models.JSONField()

class AgenteImobiliarioProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # imoveis_gerenciados = models.ManyToManyField(Imovel)

class InquilinoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)