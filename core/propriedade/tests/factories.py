from factory import Faker as FactoryFaker
from factory import Iterator
from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from core.propriedade.models import Cidade
from core.propriedade.models import Estado
from core.propriedade.models import Foto
from core.propriedade.models import Imovel
from core.propriedade.models import ImovelTipo
from core.propriedade.models import Status
from core.propriedade.models import TipoDeContrato
from core.propriedade.models import TipoDeImovel
from core.users.tests.factories import ProprietarioFactory
from core.users.tests.factories import UserFactory

fake = Faker()


class CidadeFactory(DjangoModelFactory):
    nome = FactoryFaker("city", locale="pt_BR")
    estado = SubFactory("core.propriedade.tests.factories.EstadoFactory")

    class Meta:
        model = Cidade
        django_get_or_create = ("nome",)


class EstadoFactory(DjangoModelFactory):
    nome = FactoryFaker("state")
    uf = FactoryFaker("state_abbr")

    class Meta:
        model = Estado
        django_get_or_create = ("nome", "uf")


class TipoDeImovelFactory(DjangoModelFactory):
    nome = FactoryFaker("word")
    tipo = Iterator([choice[0] for choice in ImovelTipo.choices])

    class Meta:
        model = TipoDeImovel


class ImovelFactory(DjangoModelFactory):
    proprietario = SubFactory(ProprietarioFactory)
    cidade = SubFactory(CidadeFactory)
    criado_por = SubFactory(UserFactory)
    tipo = SubFactory(TipoDeImovelFactory)
    endereco = FactoryFaker("address")
    pais = FactoryFaker("country")
    cep = FactoryFaker("postcode")
    titulo = FactoryFaker("sentence", nb_words=4)
    descricao = FactoryFaker("paragraph")
    tipo_de_contrato = Iterator([choice[0] for choice in TipoDeContrato.choices])
    status = Iterator([choice[0] for choice in Status.choices])
    preco = FactoryFaker("pydecimal", left_digits=7, right_digits=2, positive=True)
    preco_locacao = FactoryFaker(
        "pydecimal", left_digits=7, right_digits=2, positive=True
    )
    area = FactoryFaker("pydecimal", left_digits=4, right_digits=2, positive=True)
    quartos = FactoryFaker("random_int", min=1, max=10)
    banheiros = FactoryFaker("random_int", min=1, max=10)
    vagas = FactoryFaker("random_int", min=0, max=5)
    iptu = FactoryFaker("pydecimal", left_digits=5, right_digits=2, positive=True)
    condominio = FactoryFaker("pydecimal", left_digits=5, right_digits=2, positive=True)

    class Meta:
        model = Imovel


class FotoFactory(DjangoModelFactory):
    imovel = SubFactory(ImovelFactory)
    foto = FactoryFaker("image_url")

    class Meta:
        model = Foto
