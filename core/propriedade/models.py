from django.db import models

from core.users.models import Proprietario
from core.users.models import User

# Create your models here.


class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    uf = models.CharField(max_length=2, unique=True)

    class Meta:
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cidades"
        unique_together = ("estado", "nome")

    def __str__(self):
        return f"{self.nome} - {self.estado.uf}"


def upload_foto_to(instance, filename):
    return f"imoveis/{instance.imovel.endereco}/{filename}"


class Foto(models.Model):
    imovel = models.ForeignKey("Imovel", on_delete=models.CASCADE, related_name="fotos")
    foto = models.ImageField(upload_to=upload_foto_to, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Fotos"

    def __str__(self):
        return self.foto


class Status(models.TextChoices):
    RASCUNHO = "R", "Rascunho"
    PUBLICADO = "P", "Publicado"
    ARQUIVADO = "A", "Arquivado"


class TipoDeContrato(models.TextChoices):
    LOCACAO = "L", "Locação"
    VENDA = "V", "Venda"
    LANCAMENTO = "N", "Lançamentos"
    LEILAO = "E", "Leilão"
    LOCACAO_VENDA = "O", "Locação e Venda"


class ImovelTipo(models.TextChoices):
    RESIDENCIAL = "R", "Residencial"
    COMERCIAL = "C", "Comercial"


class TipoDeImovel(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=ImovelTipo.choices)

    class Meta:
        verbose_name_plural = "Tipos de Imóveis"

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"


class Imovel(models.Model):
    proprietario = models.ForeignKey(
        Proprietario, on_delete=models.CASCADE, related_name="propriedades", null=True
    )
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name="imoveis")
    criado_por = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="imoveis_criados"
    )
    tipo = models.ForeignKey(
        TipoDeImovel, on_delete=models.CASCADE, related_name="imoveis_tipo"
    )
    endereco = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo_de_contrato = models.CharField(max_length=1, choices=TipoDeContrato.choices)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.RASCUNHO,
        help_text="Status da propriedade",
    )
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="preço de venda", null=True
    )
    preco_locacao = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="preço de locação", null=True
    )
    area = models.DecimalField(max_digits=10, decimal_places=2, help_text="em m²")
    quartos = models.IntegerField()
    banheiros = models.IntegerField()
    vagas = models.IntegerField(null=True)
    iptu = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="em R$", null=True
    )
    condominio = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="em R$", null=True
    )

    class Meta:
        verbose_name_plural = "Imóveis"

    def __str__(self):
        return self.titulo
