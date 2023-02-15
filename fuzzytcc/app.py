from flask import Flask
from fuzzytcc.ext import configuracao

def minimal_app(**config):
    app = Flask(__name__)
    configuracao.init_app(app, **config)
    return app

def create_app(**config):
    app = minimal_app(**config)
    configuracao.carregar_extensoes(app)
    return 