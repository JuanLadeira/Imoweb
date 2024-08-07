from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from core.users.api.views.agente_imobilario_viewset import (
    AgenteImobiliarioProfileViewSet,
)
from core.users.api.views.cliente_viewset import ClienteProfileViewSet
from core.users.api.views.inquilino_viewset import InquilinoProfileViewSet
from core.users.api.views.user_viewset import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("agentes", AgenteImobiliarioProfileViewSet, basename="agentes")
router.register("clientes", ClienteProfileViewSet, basename="clientes")
router.register("inquilinos", InquilinoProfileViewSet, basename="inquilinos")


app_name = "api"
urlpatterns = router.urls
