from rest_framework import mixins
from rest_framework import viewsets


class CreateUpdateDestroyViewSet(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    Esta classe é um viewset customizado que implementa as operações de CRUD.
    """


class ListRetrieveUpdateViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Esta classe é um viewset customizado que implementa as operações de List, Retrieve e Update.
    """


class RetrieveUpdateViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Esta classe é um viewset customizado que implementa as operações de Retrieve e Update.
    """


class UpdateViewSet(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Esta classe é um viewset customizado que implementa a operação de Update.
    """
