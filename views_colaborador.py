# -*- coding: utf-8 -*-

from flask import *
from orm.orm_colaborador import ColaboradorORM
from models.models_colaborador import Colaborador
from __init__ import *

ACTION = 'add'
TIPOS = [u'Funcionário', u'Estágiario', u'Prestador de Serviços']
DEPARTAMENTOS = [u'Técnologia da Informação', 
                 'Comercial', 
                 'Departamento Pessoal', 
                 'Faturamento', 
                 'Financeiro', 
                 'Fiscal', 
                 'Operacional', 
                 'Diretoria', 
                 'Contabilidade', 
                 'Oficina', 
                 'Arquivamento', 
                 'Contas a Pagar',
                 'Contas a Receber',
                 'Caixa',
                 'Recursos Humanos',
                 'Outros']

@app.route('/list_colaborador')
def list_colaborador():
    cols = ColaboradorORM().query_all()    
    return render_template('colaborador_table.html', list=cols)


@app.route('/add_colaborador')
def add_colaborador ():
    col = None
    ACTION = 'add'    
    return render_template('colaborador_form.html', col=col, action=ACTION, 
        tipos=TIPOS, departamentos=DEPARTAMENTOS)


@app.route('/edit_colaborador/<p_id>')
def edit_colaborador(p_id):
    col = ColaboradorORM().query_filter_id(p_id)
    ACTION = 'edit'

    # configuracao do tipo cadastrado
    new_tipos = [col.tipo]
    for tp in TIPOS:
        if tp != col.tipo:
            new_tipos += [tp]

    # consiguracao do departamento cadastrado
    new_departamentos = [col.departamento]
    for dpto in DEPARTAMENTOS:
        if dpto != col.departamento:
            new_departamentos += [dpto]


    return render_template('colaborador_form.html', col=col, action=ACTION, tipos=new_tipos, 
        departamentos=new_departamentos)


@app.route('/save_colaborador/<p_action>', methods=['GET', 'POST'])
def save_colaborador(p_action):
    if request.method == 'POST':
        col = Colaborador(request.form['nome'], request.form['tipo'], request.form['departamento'])
        if p_action == 'edit':
             col.id = request.form['id']

        ColaboradorORM().save(col, p_action)
    else:
        return render_template('colaborador_form.html')    

    cols = ColaboradorORM().query_all()
    return render_template('colaborador_table.html', list=cols)


@app.route('/delete_colaborador/<p_colid>', methods=['GET', 'POST'])
def delete_colaborador(p_colid):
    ColaboradorORM().delete(p_colid)
    cols = ColaboradorORM().query_all()
    return render_template('colaborador_table.html', list=cols)