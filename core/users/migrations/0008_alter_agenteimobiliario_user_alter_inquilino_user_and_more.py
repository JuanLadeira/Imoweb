# Generated by Django 4.2.11 on 2024-08-21 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_contato_user_telefone_user_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenteimobiliario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inquilino', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proprietario', to=settings.AUTH_USER_MODEL),
        ),
    ]
