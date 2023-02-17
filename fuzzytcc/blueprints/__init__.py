from flask import Blueprint
from .aluno import listar_alunos, cadastrar_aluno, editar_aluno, deletar_aluno

bp_aluno = Blueprint('aluno', __name__, template_folder='templates', static_folder='static')
bp_aluno.add_url_rule('/alunos', view_func=listar_alunos, methods=['GET'])
bp_aluno.add_url_rule('/alunos/cadastro', view_func=cadastrar_aluno, methods=['GET','POST'])
bp_aluno.add_url_rule('/alunos/editar/<aluno>', view_func=editar_aluno, methods=['GET','POST'])
bp_aluno.add_url_rule('/alunos/deletar', view_func=deletar_aluno, methods=['POST'])

def init_app(app):
    app.register_blueprint(bp_aluno)