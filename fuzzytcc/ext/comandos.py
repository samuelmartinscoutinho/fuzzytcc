from fuzzytcc.ext.database import db
from fuzzytcc.models.models import *

def create_db():
    db.create_all()
    
def drob_db():
    db.drop_all()
    
def init_app(app):
    for comando in [create_db,drob_db]:
        app.cli.add_command(app.cli.command()(comando))