from django.apps import AppConfig


class CategoryConfig(AppConfig):
    name = 'api.category' #Since this is a submodule app, preface with "api." ie the parent module.
