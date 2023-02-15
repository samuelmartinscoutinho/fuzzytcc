from flask import Flask
from fuzzytcc.ext import config

def minimal_app(**config):
    app = Flask(__name__)
    config.init_app(app, **config)
    return app

def create_app(**config):
    app = minimal_app(**config)
    config.carregar_extensoes(app)
    return 