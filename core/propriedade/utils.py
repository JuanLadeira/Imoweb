from import_export.formats.base_formats import XLSX


def generate_xlsx_from_resource(resource, queryset):
    # Exporta a queryset usando o resource fornecido
    dataset = resource.export(queryset)

    # Gera os dados XLSX usando a classe XLSX do import_export
    xlsx_format = XLSX()
    return xlsx_format.export_data(dataset)
