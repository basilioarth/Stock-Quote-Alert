from django.apps import AppConfig
import os

class StockQuotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock_quotes'
    
    def ready(self):
        alredy_reload = os.environ.get('WERKZEUG_RUN_MAIN') 
        if alredy_reload is None:
            from . import tasks
            tasks.start()
            os.environ['WERKZEUG_RUN_MAIN'] = 'True'
            return
        
