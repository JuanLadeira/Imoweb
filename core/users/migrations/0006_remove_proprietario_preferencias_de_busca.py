# Generated by Django 4.2.11 on 2024-08-17 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_user_type_user_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proprietario',
            name='preferencias_de_busca',
        ),
    ]