from django.urls import path

from core.authentication.views import login_view
from core.authentication.views import logout_view
from core.authentication.views import refresh_token_view
from core.authentication.views import verify_token_view

urlpatterns = [
    path(
        route="token/",
        view=login_view.LoginView.as_view(),
        name="token_obtain_pair",
    ),
    path(route="token/logout", view=logout_view.logout_view, name="logout"),
    path(
        route="token/refresh/",
        view=refresh_token_view.RefreshTokenView.as_view(),
        name="token_refresh",
    ),
    path(
        route="token/verify/",
        view=verify_token_view.TokenVerifyView.as_view(),
        name="token_verify",
    ),
]
