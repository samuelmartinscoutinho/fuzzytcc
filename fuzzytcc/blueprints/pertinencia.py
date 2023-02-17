from flask import request, render_template, flash, redirect, url_for
from fuzzytcc.models.models import Pertinencia
from fuzzytcc.ext.database import db

def cadastrar_pertinencia():
    if request.method == 'GET':
        pertinencia = Pertinencia.query.first()
        return render_template('cadastro_pertinencia.html', pertinencia=pertinencia)
    elif request.method == 'POST':
        imc_baixo = request.form.get('imcBaixo')
        imc_medio = request.form.get('imcMedio')
        imc_alto = request.form.get('imcAlto')
        percentual_gordura_baixo = request.form.get('percentualGorduraBaixo')
        percentual_gordura_medio = request.form.get('percentualGorduraMedio')
        percentual_gordura_alto = request.form.get('percentualGorduraAlto')
        percentual_massa_baixo = request.form.get('percentualMassaBaixo')
        percentual_massa_medio = request.form.get('percentualMassaMedio')
        percentual_massa_alto = request.form.get('percentualMassaAlto')
        
        pertinencia = Pertinencia.query.first()
        
        if pertinencia is None:
            try:
                nova_pertinencia = Pertinencia(
                    imc_baixo=imc_baixo,
                    imc_medio=imc_medio,
                    imc_alto=imc_alto,
                    percentual_gordura_baixo=percentual_gordura_baixo,
                    percentual_gordura_medio=percentual_gordura_medio,
                    percentual_gordura_alto=percentual_gordura_alto,
                    percentual_massa_baixo=percentual_massa_baixo,
                    percentual_massa_medio=percentual_massa_medio,
                    percentual_massa_alto = percentual_massa_alto
                )
                db.session.add(nova_pertinencia)
                db.session.commit()
                
                flash('Pertiencia cadastrada com sucesso!', 'success')
                return redirect(url_for(f'pertinencia.cadastrar_pertinencia'))
                
            except Exception as expt:
                db.session.rollback()
                flash('Não foi possivel cadastrar a pertinencia! Tente novamente!', 'danger')
                return redirect(url_for(f'pertinencia.cadastrar_pertinencia'))
        else:
            try:
                pertinencia.imc_baixo=imc_baixo
                pertinencia.imc_medio=imc_medio
                pertinencia.imc_alto=imc_alto
                pertinencia.percentual_gordura_baixo=percentual_gordura_baixo
                pertinencia.percentual_gordura_medio=percentual_gordura_medio
                pertinencia.percentual_gordura_medio=percentual_gordura_medio
                pertinencia.percentual_massa_baixo=percentual_massa_baixo
                pertinencia.percentual_massa_medio=percentual_massa_medio
                pertinencia.percentual_massa_alto=percentual_massa_alto
                
                db.session.commit()
                
                flash('Pertiencia editada com sucesso!', 'success')
                return redirect(url_for(f'pertinencia.cadastrar_pertinencia'))
            except Exception as expt:
                db.session.rollback()
                flash('Não foi possivel editar a pertinencia! Tente novamente!', 'danger')
                return redirect(url_for(f'pertinencia.cadastrar_pertinencia'))