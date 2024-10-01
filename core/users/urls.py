from django.conf import settings
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from core.users.api.views.agente_imobilario_viewset import AgenteImobiliarioViewSet
from core.users.api.views.inquilino_viewset import InquilinoViewSet
from core.users.api.views.proprietario_viewset import ProprietarioViewSet
from core.users.api.views.user_logged_in_viewset import user_logged_in_view

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("agentes", AgenteImobiliarioViewSet, basename="agentes")
router.register("proprietarios", ProprietarioViewSet, basename="proprietarios")
router.register("inquilinos", InquilinoViewSet, basename="inquilinos")


app_name = "users"

urlpatterns = [
    path("", include(router.urls)),
    path("user_logged_in/", user_logged_in_view, name="user_logged_in"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
