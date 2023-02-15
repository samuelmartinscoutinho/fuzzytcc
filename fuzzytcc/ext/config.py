from importlib import import_module
from dynaconf import FlaskDynaconf

def carregar_extensoes(app):
    for extensao in app.config.EXTENSIONS:
        nome_modulo, factory = extensao.split(":")
        ext = import_module(nome_modulo)
        getattr(ext, factory)(app)
        
def init_app(app, **config):
    FlaskDynaconf(app, **config)