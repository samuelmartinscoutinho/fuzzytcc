from flask import Blueprint
from .aluno import *
from .professor import *
from .pertinencia import *

bp_aluno = Blueprint('aluno', __name__, template_folder='templates', static_folder='static')
bp_aluno.add_url_rule('/alunos', view_func=listar_alunos, methods=['GET'])
bp_aluno.add_url_rule('/alunos/cadastro', view_func=cadastrar_aluno, methods=['GET','POST'])
bp_aluno.add_url_rule('/alunos/editar/<aluno>', view_func=editar_aluno, methods=['GET','POST'])
bp_aluno.add_url_rule('/alunos/deletar', view_func=deletar_aluno, methods=['POST'])

bp_professor = Blueprint('professor', __name__, template_folder='templates', static_folder='static')
bp_professor.add_url_rule('/professores', view_func=listar_professores, methods=['GET'])
bp_professor.add_url_rule('/professores/cadastro', view_func=cadastrar_professor, methods=['GET','POST'])
bp_professor.add_url_rule('/professores/editar/<professor>', view_func=editar_professor, methods=['GET','POST'])
bp_professor.add_url_rule('/professores/deletar', view_func=deletar_professor, methods=['POST'])

bp_pertinencia = Blueprint('pertinencia', __name__, template_folder='templates', static_folder='static')
bp_pertinencia.add_url_rule('/pertinencia/cadastro', view_func=cadastrar_pertinencia, methods=['GET', 'POST'])

def init_app(app):
    app.register_blueprint(bp_aluno)
    app.register_blueprint(bp_professor)
    app.register_blueprint(bp_pertinencia)