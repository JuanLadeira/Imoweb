from django.db import models

from core.users.models import Proprietario
from core.users.models import User

# Create your models here.


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    foto = models.ImageField(upload_to="fotos", null=True, blank=True)

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

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    proprietario = models.ForeignKey(
        Proprietario, on_delete=models.CASCADE, related_name="propriedades"
    )
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name="imoveis")
    criado_por = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="imoveis_criados"
    )
    foto = models.ForeignKey(
        Foto, on_delete=models.CASCADE, related_name="imoveis_fotos"
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

    def __str__(self):
        return self.titulo
