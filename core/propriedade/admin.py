from django.contrib import admin
from import_export import fields
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline
from unfold.contrib.import_export.forms import ExportForm
from unfold.contrib.import_export.forms import ImportForm

from core.propriedade.models import Cidade
from core.propriedade.models import Estado
from core.propriedade.models import Foto
from core.propriedade.models import Imovel
from core.propriedade.models import Status
from core.propriedade.models import TipoDeImovel


class ImovelResource(resources.ModelResource):
    status = fields.Field(
        column_name="status",
        attribute="status",
    )

    def dehydrate_status(self, imovel):
        # Retorna a label do status a partir dos choices definidos
        return imovel.get_status_display()

    class Meta:
        model = Imovel
        import_id_fields = ("id",)
        fields = (
            "id",
            "titulo",
            "status",
            "endereco",
            "valor",
        )  # Defina as colunas desejadas
        export_order = (
            "id",
            "titulo",
            "status",
            "endereco",
            "valor",
        )  # Ordem das colunas no CSV


@admin.register(Cidade)
class CidadeAdmin(ModelAdmin):
    list_display = ("nome", "estado")
    search_fields = ("nome", "estado__nome")
    list_filter = ("estado",)
    list_per_page = 10
    ordering = ("nome",)


@admin.register(Estado)
class EstadoAdmin(ModelAdmin):
    list_display = ("nome", "uf")
    search_fields = ("nome", "uf")
    list_per_page = 10
    ordering = ("nome",)


class FotoInline(TabularInline):
    model = Foto
    extra = 1
    fields = ("foto",)
    readonly_fields = ("imovel",)


class StatusFilter(admin.SimpleListFilter):
    title = "status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return Status.choices

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset


@admin.register(Imovel)
class ImovelAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_class = ImovelResource
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = (
        "titulo",
        "status",
        "tipo_de_contrato",
        "preco",
        "proprietario",
        "cidade",
        "get_tipo_imovel",
    )
    search_fields = (
        "titulo",
        "status",
        "tipo_de_contrato",
        "preco",
        "cidade__nome",
        "proprietario__nome",
        "tipo__nome",
    )
    list_filter = (StatusFilter, "tipo_de_contrato", "cidade", "tipo")
    list_per_page = 10
    ordering = ("titulo",)
    inlines = [FotoInline]
    fieldsets = (
        (
            "Informações Básicas",
            {
                "fields": (
                    "titulo",
                    "descricao",
                    "tipo",
                    "tipo_de_contrato",
                    "status",
                    "proprietario",
                    "cidade",
                )
            },
        ),
        ("Localização", {"fields": ("endereco", "pais", "cep")}),
        ("Valores", {"fields": ("preco", "preco_locacao", "iptu", "condominio")}),
        ("Características", {"fields": ("area", "quartos", "banheiros", "vagas")}),
    )
    readonly_fields = ("criado_por", "status")
    actions = ["publicar_imovel", "arquivar_imovel"]

    def save_model(self, request, obj, form, change):
        if not change or not obj.criado_por:
            obj.criado_por = request.user

        super().save_model(request, obj, form, change)

    @admin.display(description="Tipo de Imóvel")
    def get_tipo_imovel(self, obj):
        return obj.tipo.nome

    @admin.action(description="Publicar imóveis selecionados")
    def publicar_imovel(self, request, queryset):
        queryset.update(status=Status.PUBLICADO)

    @admin.action(description="Arquivar imóveis selecionados")
    def arquivar_imovel(self, request, queryset):
        queryset.update(status=Status.ARQUIVADO)


@admin.register(Foto)
class FotoAdmin(ModelAdmin):
    list_display = ("imovel", "foto")
    search_fields = ("imovel__titulo",)
    list_filter = ("imovel",)
    list_per_page = 10


@admin.register(TipoDeImovel)
class TipoDeImovelAdmin(ModelAdmin):
    list_display = ("nome", "tipo")
    search_fields = ("nome", "tipo")
    list_per_page = 10
    ordering = ("nome",)
