# Generated by Django 4.2.11 on 2024-10-01 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_remove_agenteimobiliario_id_remove_inquilino_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeImovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('R', 'Residencial'), ('C', 'Comercial')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('tipo_de_contrato', models.CharField(choices=[('L', 'Locação'), ('V', 'Venda'), ('N', 'Lançamentos'), ('E', 'Leilão'), ('O', 'Locação e Venda')], max_length=1)),
                ('status', models.CharField(choices=[('R', 'Rascunho'), ('P', 'Publicado'), ('A', 'Arquivado')], default='R', help_text='Status da propriedade', max_length=1)),
                ('preco', models.DecimalField(decimal_places=2, help_text='preço de venda', max_digits=10, null=True)),
                ('preco_locacao', models.DecimalField(decimal_places=2, help_text='preço de locação', max_digits=10, null=True)),
                ('area', models.DecimalField(decimal_places=2, help_text='em m²', max_digits=10)),
                ('quartos', models.IntegerField()),
                ('banheiros', models.IntegerField()),
                ('vagas', models.IntegerField(null=True)),
                ('iptu', models.DecimalField(decimal_places=2, help_text='em R$', max_digits=10, null=True)),
                ('condominio', models.DecimalField(decimal_places=2, help_text='em R$', max_digits=10, null=True)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imoveis', to='propriedade.cidade')),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imoveis_criados', to=settings.AUTH_USER_MODEL)),
                ('foto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imoveis_fotos', to='propriedade.foto')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propriedades', to='users.proprietario')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imoveis_tipo', to='propriedade.tipodeimovel')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propriedade.estado'),
        ),
    ]
