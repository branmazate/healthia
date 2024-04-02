from django.apps import AppConfig

class HealthiaConfig(AppConfig):
    name = 'healthia'
    
    def ready(self):
        import healthia.signals