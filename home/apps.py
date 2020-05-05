from django.apps import AppConfig


class HomepageConfig(AppConfig):
    name = 'home'
    def ready(self):
        from stockUpdater import updater
        updater.start()
