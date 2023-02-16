from flask import request, render_template, flash
from fuzzytcc.models.models import Usuario,Aluno
from fuzzytcc.ext.database import db

def cadastrar_aluno():
    if request.method == 'GET':
        return render_template('cadastro_aluno.html')
    
    elif request.method == 'POST':
        nome = request.form.get('nomeAluno')
        genero = request.form.get('generoAluno')
        login = request.form.get('loginAluno')
        email = request.form.get('emailAluno')
        senha = request.form.get('senhaAluno')
    
        try:
            novo_usuario = Usuario(
                login=login, 
                senha=senha, 
                email=email,
                eadmin=False
                )
            db.session.add(novo_usuario)
            db.session.commit()
            db.session.flush()
            
            novo_usuario = novo_usuario.id
            novo_usuario = Usuario.query.filter_by(id=novo_usuario).first()
        
            novo_aluno = Aluno(
                nome=nome,
                genero=genero,
                usuario=novo_usuario
            )
        
            db.session.add(novo_aluno)
            db.session.commit()
        
            flash('Aluno cadastrado com sucesso!', 'success')
            return render_template('listagem_aluno.html')
    
        except Exception as expt:
            print(expt)
            db.session.rollback()
            
            flash('Não foi possivel cadastrar o aluno! Tente novamente!', 'danger')
            return render_template('cadastro_aluno.html')
    