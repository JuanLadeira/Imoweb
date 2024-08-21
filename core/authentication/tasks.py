# tasks.py
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_reset_password_email(email, token):
    """
    Tarefa Celery para enviar um email de redefinição de senha.

    Parâmetros:
        email (str): O email do usuário.
        token (str): O token de redefinição de senha.
    """
    send_mail(
        "Redefinição de senha",
        f"Aqui está o seu token de redefinição de senha: {token}",
        "from@example.com",
        [email],
    )
