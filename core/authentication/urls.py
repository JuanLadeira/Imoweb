from django.urls import path

from core.authentication.views import forgot_password_view
from core.authentication.views import login_view
from core.authentication.views import logout_view
from core.authentication.views import refresh_token_view
from core.authentication.views import reset_password_view
from core.authentication.views import verify_token_view

urlpatterns = [
    path(
        route="token/",
        view=login_view.LoginView.as_view(),
        name="token_obtain_pair",
    ),
    path(route="logout/", view=logout_view.logout_view, name="logout"),
    path(
        route="token/refresh/",
        view=refresh_token_view.RefreshTokenView.as_view(),
        name="token_refresh",
    ),
    path(
        route="token/verify/",
        view=verify_token_view.VerifyTokenView.as_view(),
        name="token_verify",
    ),
    path(
        route="forgot-password/",
        view=forgot_password_view.ForgotPasswordView.as_view(),
        name="forgot_password",
    ),
    path(
        route="reset-password/",
        view=reset_password_view.ResetPasswordView.as_view(),
        name="reset_password",
    ),
]
