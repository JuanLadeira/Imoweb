# Generated by Django 4.2.11 on 2024-10-01 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_agenteimobiliario_user_alter_inquilino_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenteimobiliario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='inquilino',
            name='id',
        ),
        migrations.RemoveField(
            model_name='proprietario',
            name='id',
        ),
        migrations.AlterField(
            model_name='agenteimobiliario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='agente', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='inquilino', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='proprietario', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
