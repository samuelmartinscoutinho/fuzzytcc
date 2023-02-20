from flask import request, render_template, flash, redirect, url_for
from fuzzytcc.models.models import Regra
from fuzzytcc.ext.database import db

def listar_regras():
    regras = Regra.query.order_by(Regra.id).all()
    return render_template('listagem_regra.html', regras=regras)

def cadastrar_regra():
    if request.method == 'GET':
        return render_template('cadastro_regra.html')
    elif request.method == 'POST':
        a = []
        operador = request.form.get('operador')
        imc_baixo = True if request.form.get('imcBaixo')is not None else False
        imc_medio = True if request.form.get('imcMedio') is not None else False
        imc_alto = True if request.form.get('imcAlto') is not None else False
        percentual_gordura_baixo = True if request.form.get('percentualGorduraBaixo') is not None else False
        percentual_gordura_medio = True if request.form.get('percentualGorduraMedio') is not None else False
        percentual_gordura_alto = True if request.form.get('percentualGorduraAlto') is not None else False
        percentual_massa_baixo = True if request.form.get('percentualMassaBaixo') is not None else False
        percentual_massa_medio = True if request.form.get('percentualMassaMedio') is not None else False
        percentual_massa_alto = True if request.form.get('percentualMassaAlto') is not None else False
        efumante = True if request.form.get('efumante') is not None else False
        ehipertenso = True if request.form.get('ehipertenso') is not None else False
        ediabetico = True if request.form.get('ediabetico') is not None else False
        regra_portugues = request.form.get('regra')
        treino = request.form.get('treino')
        quantidade_tempo = request.form.get('tempo')
        
        if imc_baixo:
          a.append("a[[i for i in range(len(a)) if (a[i]['id']=='imc')][0]]['Valor'][0][0]")
        if imc_medio:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='imc')][0]]['Valor'][0][1]")
        if imc_alto:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='imc')][0]]['Valor'][0][2]")
            
        if percentual_gordura_baixo:
          a.append("a[[i for i in range(len(a)) if (a[i]['id']=='pgordura')][0]]['Valor'][0][0]")
        if percentual_gordura_medio:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='pgordura')][0]]['Valor'][0][1]")
        if percentual_gordura_alto:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='pgordura')][0]]['Valor'][0][2]")
            
        if percentual_massa_baixo:
          a.append("a[[i for i in range(len(a)) if (a[i]['id']=='massa')][0]]['Valor'][0][0]")
        if percentual_massa_medio:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='massa')][0]]['Valor'][0][1]")
        if percentual_massa_alto:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='massa')][0]]['Valor'][0][2]")
            
        if efumante:
          a.append("a[[i for i in range(len(a)) if (a[i]['id']=='efumante')][0]]['Valor'][0][0]")
        if ehipertenso:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='ehipertenso')][0]]['Valor'][0][0]")
        if ediabetico:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='ediabetico')][0]]['Valor'][0][0]")
            
        regra_fuzzy = f'max({a})' if operador == 'e' else f'min({a})' 
        
        try:
            nova_regra = Regra(
                regra_portugues=regra_portugues,
                regra_fuzzy=regra_fuzzy,
                operador=operador,
                imc_baixo=imc_baixo,
                imc_medio=imc_medio,
                imc_alto=imc_alto,
                percentual_gordura_baixo=percentual_gordura_baixo,
                percentual_gordura_medio=percentual_gordura_medio,
                percentual_gordura_alto=percentual_gordura_alto,
                percentual_massa_baixo=percentual_massa_baixo,
                percentual_massa_medio = percentual_massa_medio,
                percentual_massa_alto=percentual_massa_alto,
                efumante=efumante,
                ehipertenso=ehipertenso,
                ediabetico=ediabetico,
                treino=treino,
                tempo=quantidade_tempo)
            
            db.session.add(nova_regra)
            db.session.commit()
            flash('Regra cadastrada com sucesso!', 'success')
            return redirect(url_for('regra.listar_regras'))
        except Exception as expt:
            print(expt)
            db.session.rollback()
            flash('Não foi possivel gerar esta regra! Tente novamente', 'danger')
            return redirect(url_for('regra.cadastrar_regra'))
        
def editar_regra(regra:int):
    if request.method == 'GET':
        regra_editar = Regra.query.filter(Regra.id == regra).first()
        if regra_editar is not None:
            return render_template('editar_regra.html', regra=regra_editar, tipo_cadastro='Editar Regra')
        else:
            flash('Não foi possivel localizar estas regra! Tente outra!', 'warning')
            return redirect(url_for('regra.listar_regras'))
            
    elif request.method == 'POST':
        a = []
        operador = request.form.get('operador')
        imc_baixo = True if request.form.get('imcBaixo')is not None else False
        imc_medio = True if request.form.get('imcMedio') is not None else False
        imc_alto = True if request.form.get('imcAlto') is not None else False
        percentual_gordura_baixo = True if request.form.get('percentualGorduraBaixo') is not None else False
        percentual_gordura_medio = True if request.form.get('percentualGorduraMedio') is not None else False
        percentual_gordura_alto = True if request.form.get('percentualGorduraAlto') is not None else False
        percentual_massa_baixo = True if request.form.get('percentualMassaBaixo') is not None else False
        percentual_massa_medio = True if request.form.get('percentualMassaMedio') is not None else False
        percentual_massa_alto = True if request.form.get('percentualMassaAlto') is not None else False
        efumante = True if request.form.get('efumante') is not None else False
        ehipertenso = True if request.form.get('ehipertenso') is not None else False
        ediabetico = True if request.form.get('ediabetico') is not None else False
        regra_portugues = request.form.get('regra')
        treino = request.form.get('treino')
        quantidade_tempo = request.form.get('tempo')
        
        if imc_baixo:
          a.append("a[[i for i in range(len(a)) if (a[i]['id']=='imc')][0]]['Valor'][0][0]")
        if imc_medio:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='imc')][0]]['Valor'][0][1]")
        if imc_alto:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='imc')][0]]['Valor'][0][2]")
            
        if percentual_gordura_baixo:
          a.append("a[[i for i in range(len(a)) if (a[i]['id']=='pgordura')][0]]['Valor'][0][0]")
        if percentual_gordura_medio:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='pgordura')][0]]['Valor'][0][1]")
        if percentual_gordura_alto:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='pgordura')][0]]['Valor'][0][2]")
            
        if percentual_massa_baixo:
          a.append("a[[i for i in range(len(a)) if (a[i]['id']=='massa')][0]]['Valor'][0][0]")
        if percentual_massa_medio:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='massa')][0]]['Valor'][0][1]")
        if percentual_massa_alto:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='massa')][0]]['Valor'][0][2]")
            
        if efumante:
          a.append("a[[i for i in range(len(a)) if (a[i]['id']=='efumante')][0]]['Valor'][0][0]")
        if ehipertenso:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='ehipertenso')][0]]['Valor'][0][0]")
        if ediabetico:
            a.append("a[[i for i in range(len(a)) if (a[i]['id']=='ediabetico')][0]]['Valor'][0][0]")
            
        regra_fuzzy = f'max({a})' if operador == 'e' else f'min({a})' 
        
        regra_editar = Regra.query.filter(Regra.id == regra).first()
        
        try:
            regra_editar.regra_portugues=regra_portugues
            regra_editar.regra_fuzzy=regra_fuzzy
            regra_editar.operador = operador
            regra_editar.imc_baixo=imc_baixo
            regra_editar.imc_medio=imc_medio
            regra_editar.imc_alto=imc_alto
            regra_editar.percentual_gordura_baixo=percentual_gordura_baixo
            regra_editar.percentual_gordura_medio=percentual_gordura_medio
            regra_editar.percentual_gordura_alto=percentual_gordura_alto
            regra_editar.percentual_massa_baixo=percentual_massa_baixo
            regra_editar.percentual_massa_medio = percentual_massa_medio
            regra_editar.percentual_massa_alto=percentual_massa_alto
            regra_editar.efumante=efumante
            regra_editar.ehipertenso=ehipertenso
            regra_editar.ediabetico=ediabetico
            regra_editar.treino=treino
            regra_editar.tempo=quantidade_tempo
            
            db.session.commit()
            flash('Regra editada com sucesso!', 'success')
            return redirect(url_for('regra.listar_regras'))
        
        except Exception as expt:
            db.session.rollback()
            flash('Não foi possivel editar esta regra! Tente novamente!', 'danger')
            return redirect(url_for(f'regra.editar_regra', regra=regra))
        
def deletar_regra():
    id_regra = request.form.get('idRegra')
    try:
        Regra.query.filter(Regra.id == id_regra).delete()
        db.session.commit()
        flash('Regra deletada com sucesso!', 'success')
        return redirect(url_for('regra.listar_regras'))
    except Exception as expt:
        db.session.rollback()
        flash('Não foi possivel deletar esta regra! Tente novamente!', 'danger')
        return redirect(url_for('regra.listar_regras'))