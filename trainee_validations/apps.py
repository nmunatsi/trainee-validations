from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'trainee_validations'
    verbose_name = 'Trainee Form Validations'
