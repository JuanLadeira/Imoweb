# Generated by Django 4.2.11 on 2024-10-03 01:25

import core.propriedade.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propriedade', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='foto',
        ),
        migrations.AddField(
            model_name='foto',
            name='imovel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='propriedade.imovel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=core.propriedade.models.upload_foto_to),
        ),
    ]
