from django.apps import AppConfig


class CycleStatusConfig(AppConfig):
    name = 'cyclestatus'

    def ready(self):
        import cyclestatus.signals
