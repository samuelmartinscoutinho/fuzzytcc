from flask import request, render_template, flash, redirect, url_for
from fuzzytcc.models.models import Usuario,Aluno, Professor
from fuzzytcc.ext.database import db

def listar_professores():
    professores = db.session.query(Professor,Usuario).join(Usuario).filter(Professor.usuario==Usuario.id).order_by(Professor.nome).all()
    return render_template('listagem_professor.html',professores=professores)

def cadastrar_professor():
    if request.method == 'GET':
        return render_template('cadastro_professor.html')
    elif request.method == 'POST':
        nome = request.form.get('nomeProfessor')
        genero = request.form.get('generoProfessor')
        login = request.form.get('loginProfessor')
        email = request.form.get('emailProfessor')
        senha = request.form.get('senhaProfessor')
        
        if genero not in ['Masculino', 'Feminino']:
            flash('Não foi possivel cadastrar este professor! Pois foi informado um sexo inexistente!', 'danger')
            return redirect(url_for(f'professor.cadastrar_professor'))
    
        try:
            novo_usuario = Usuario(
                login=login, 
                senha=senha, 
                email=email,
                eadmin=False
                )
  
            novo_professor = Professor(
                nome=nome,
                genero=genero,
                usuario=novo_usuario
            )
            
            db.session.add(novo_usuario)
            db.session.add(novo_professor)
            db.session.commit()
        
            flash('Professor cadastrado com sucesso!', 'success')
            return redirect(url_for('professor.listar_professores'))
    
        except Exception as expt:
            db.session.rollback()
            flash('Não foi possivel cadastrar o professor! Tente novamente!', 'danger')
            return render_template('cadastro_professor.html')

def editar_professor(professor:int):
    if request.method == 'GET':
        professor_editar = db.session.query(Professor,Usuario).join(Usuario, Professor.usuario==Usuario.id).filter(Professor.id == professor).order_by(Professor.nome).first()
        if professor_editar is not None:
            return render_template('editar_professor.html', professor_editar=professor_editar)
        else:
            flash('Não foi possivel localizar este professor! Tente outro!', 'warning')
            return redirect(url_for('professor.listar_professores'))
            
    elif request.method == 'POST':
        nome = request.form.get('nomeProfessor')
        genero = request.form.get('generoProfessor')
        email = request.form.get('emailProfessor')
        
        if genero not in ['Masculino', 'Feminino']:
            flash('Não foi possivel editar este professor! Pois foi informado um sexo inexistente!', 'danger')
            return redirect(url_for(f'professor.editar_professor', professor=professor))
        
        professor_editar = Professor.query.filter(Professor.id == professor).first()
        usuario_editar = Usuario.query.filter(Usuario.id == professor_editar.usuario).first()
        
        try:
            professor_editar.nome = nome
            professor_editar.genero = genero
            usuario_editar.email = email
            
            db.session.commit()
            flash('Professor editado com sucesso!', 'success')
            return redirect(url_for('professor.listar_professores'))
        
        except Exception as expt:
            db.session.rollback()
            flash('Não foi possivel editar este professor! Tente novamente!', 'danger')
            return redirect(url_for(f'professor.editar_professor', professor=professor))
        
def deletar_professor():
    id_usuario = request.form.get('idProfessor')
    try:
        Professor.query.filter(Professor.usuario == id_usuario).delete()
        Usuario.query.filter(Usuario.id == id_usuario).delete()
        db.session.commit()
        flash('Professor deletado com sucesso!', 'success')
        return redirect(url_for('professor.listar_professores'))
    except Exception as expt:
        db.session.rollback()
        flash('Não foi possivel deletar este professor! Tente novamente!', 'danger')
        return redirect(url_for('professor.listar_professores'))