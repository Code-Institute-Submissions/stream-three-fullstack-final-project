from django.apps import AppConfig


class CyclePortholeConfig(AppConfig):
    name = 'cycleporthole'

    def ready(self):
        import cycleporthole.signals
        
