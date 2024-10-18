from django.conf import settings
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from core.propriedade.api.views.cidade_viewset import CidadeViewSet
from core.propriedade.api.views.estado_viewset import EstadoViewSet
from core.propriedade.api.views.foto_viewset import FotoViewSet
from core.propriedade.api.views.imovel_viewset import ImovelViewSet
from core.propriedade.api.views.tipo_imovel_viewset import TipoDeImovelViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("estados", EstadoViewSet, basename="estados")
router.register("cidades", CidadeViewSet, basename="cidades")
router.register("fotos", FotoViewSet, basename="fotos")
router.register("tipos-de-imoveis", TipoDeImovelViewSet, basename="tipos-de-imoveis")
router.register("", ImovelViewSet, basename="imoveis")


app_name = "propriedade"

urlpatterns = [
    path("", include(router.urls)),
]
