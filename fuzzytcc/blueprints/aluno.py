from flask import request, render_template, flash, redirect, url_for
from fuzzytcc.models.models import Usuario,Aluno
from fuzzytcc.ext.database import db

def listar_alunos():
    alunos = db.session.query(Aluno,Usuario).join(Usuario).filter(Aluno.usuario==Usuario.id).order_by(Aluno.nome).all()
    return render_template('listagem_aluno.html',alunos=alunos)

def cadastrar_aluno():
    if request.method == 'GET':
        return render_template('registro_aluno.html', aluno=(None, None), tipo_cadastro ='Cadastrar Aluno')
    elif request.method == 'POST':
        nome = request.form.get('nomeAluno')
        genero = request.form.get('generoAluno')
        login = request.form.get('loginAluno')
        email = request.form.get('emailAluno')
        senha = request.form.get('senhaAluno')
        
        if genero not in ['Masculino', 'Feminino']:
            flash('Não foi possivel cadastrar este aluno! Pois foi informado um sexo inexistente!', 'danger')
            return redirect(url_for(f'aluno.cadastrar_aluno'))
    
        try:
            novo_usuario = Usuario(
                login=login, 
                senha=senha, 
                email=email,
                eadmin=False
                )
  
            novo_aluno = Aluno(
                nome=nome,
                genero=genero,
                usuario=novo_usuario
            )
            
            db.session.add(novo_usuario)
            db.session.add(novo_aluno)
            db.session.commit()
        
            flash('Aluno cadastrado com sucesso!', 'success')
            return redirect(url_for('aluno.listar_alunos'))
    
        except Exception as expt:
            db.session.rollback()
            flash('Não foi possivel cadastrar o aluno! Tente novamente!', 'danger')
            return render_template('registro_aluno.html')

def editar_aluno(aluno:int):
    if request.method == 'GET':
        aluno_editar = db.session.query(Aluno,Usuario).join(Usuario, Aluno.usuario==Usuario.id).filter(Aluno.id == aluno).order_by(Aluno.nome).first()
        if aluno_editar is not None:
            return render_template('registro_aluno.html', aluno=aluno_editar, tipo_cadastro='Editar Aluno')
        else:
            flash('Não foi possivel localizar este aluno! Tente outro!', 'warning')
            return redirect(url_for('aluno.listar_alunos'))
            
    elif request.method == 'POST':
        nome = request.form.get('nomeAluno')
        genero = request.form.get('generoAluno')
        email = request.form.get('emailAluno')
        
        if genero not in ['Masculino', 'Feminino']:
            flash('Não foi possivel editar este aluno! Pois foi informado um sexo inexistente!', 'danger')
            return redirect(url_for(f'aluno.editar_aluno', aluno=aluno))
        
        aluno_editar = Aluno.query.filter(Aluno.id == aluno).first()
        usuario_editar = Usuario.query.filter(Usuario.id == aluno_editar.usuario).first()
        
        try:
            aluno_editar.nome = nome
            aluno_editar.genero = genero
            usuario_editar.email = email
            
            db.session.commit()
            flash('Aluno editado com sucesso!', 'success')
            return redirect(url_for('aluno.listar_alunos'))
        
        except Exception as expt:
            db.session.rollback()
            flash('Não foi possivel editar este aluno! Tente novamente!', 'danger')
            return redirect(url_for(f'aluno.editar_aluno', aluno=aluno))
        
def deletar_aluno():
    id_usuario = request.form.get('idAluno')
    try:
        Aluno.query.filter(Aluno.usuario == id_usuario).delete()
        Usuario.query.filter(Usuario.id == id_usuario).delete()
        db.session.commit()
        flash('Aluno deletado com sucesso!', 'success')
        return redirect(url_for('aluno.listar_alunos'))
    except Exception as expt:
        print(expt)
        db.session.rollback()
        flash('Não foi possivel deletar este aluno! Tente novamente!', 'danger')
        return redirect(url_for('aluno.listar_alunos'))