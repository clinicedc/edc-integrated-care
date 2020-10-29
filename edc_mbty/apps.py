from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "edc_mbty"
    verbose_name = "Edc Morbidities"
    has_exportable_data = False
    include_in_administration_section = False
