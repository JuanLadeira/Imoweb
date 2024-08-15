import uuid

from factory import Faker as FactoryFaker
from factory import PostGenerationMethodCall
from factory import Sequence as SequenceFactory
from factory import SubFactory
from factory import post_generation
from factory.django import DjangoModelFactory
from faker import Faker

from core.users.models import AgenteImobiliario
from core.users.models import Inquilino
from core.users.models import Proprietario
from core.users.models import User

fake = Faker()


class UserFactory(DjangoModelFactory):
    username = SequenceFactory(lambda n: fake.user_name() + str(uuid.uuid4())[:4])
    email = FactoryFaker("email")
    first_name = FactoryFaker("first_name")
    last_name = FactoryFaker("last_name")
    password = PostGenerationMethodCall("set_password", "test")

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """Save again the instance if creating and at least one hook ran."""
        if create and results and not cls._meta.skip_postgeneration_save:
            # Some post-generation hooks ran, and may have modified us.
            instance.save()

    class Meta:
        model = User
        django_get_or_create = ["username"]


class ProprietarioFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    preferencias_de_busca = FactoryFaker("sentence", nb_words=10)

    class Meta:
        model = Proprietario

    @post_generation
    def set_tipo(self, create, extracted, **kwargs):
        if not create:
            return
        self.user.tipo = "proprietario"
        self.user.save()


class InquilinoFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)

    class Meta:
        model = Inquilino

    @post_generation
    def set_tipo(self, create, extracted, **kwargs):
        if not create:
            return
        self.user.tipo = "inquilino"
        self.user.save()


class AgenteImobiliarioFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)

    class Meta:
        model = AgenteImobiliario

    @post_generation
    def set_tipo(self, create, extracted, **kwargs):
        if not create:
            return
        self.user.tipo = "agente"
        self.user.save()
