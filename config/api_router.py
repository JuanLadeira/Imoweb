from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from core.users.api.views.agente_imobilario_viewset import AgenteImobiliarioViewSet
from core.users.api.views.inquilino_viewset import InquilinoViewSet
from core.users.api.views.proprietario_viewset import ProprietarioViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("agentes", AgenteImobiliarioViewSet, basename="agentes")
router.register("proprietarios", ProprietarioViewSet, basename="proprietarios")
router.register("inquilinos", InquilinoViewSet, basename="inquilinos")


app_name = "api"
urlpatterns = router.urls
