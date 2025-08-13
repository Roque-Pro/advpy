from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
from datetime import datetime
import os
from models import Demanda
from extensions import db
from utils import login_required, normalizar_nome, gerar_resposta_ia
from config import UPLOAD_FOLDER

# Nome do blueprint corrigido para 'demandas'
demandas_bp = Blueprint('demandas', __name__)

FASES = ['Inicial', 'Contestação', 'Réplica', 'Sentença']

@demandas_bp.route('/')
@login_required
def painel():
    demandas = Demanda.query.order_by(Demanda.data_entrada.desc()).all()
    return render_template('painel.html', demandas=demandas)

@demandas_bp.route('/demanda/<int:id>')
@login_required
def ver_demanda(id):
    demanda = Demanda.query.get_or_404(id)
    demanda_folder = os.path.join(UPLOAD_FOLDER, str(id))
    arquivos = os.listdir(demanda_folder) if os.path.exists(demanda_folder) else []
    return render_template('ver_demanda.html', demanda=demanda, arquivos=arquivos)

@demandas_bp.route('/upload/<int:id>', methods=['POST'])
@login_required
def upload_arquivo(id):
    if 'arquivo' not in request.files:
        flash('Nenhum arquivo enviado.')
        return redirect(url_for('demandas.ver_demanda', id=id))

    file = request.files['arquivo']
    if file.filename == '':
        flash('Nenhum arquivo selecionado.')
        return redirect(url_for('demandas.ver_demanda', id=id))

    filename = normalizar_nome(file.filename)
    demanda_folder = os.path.join(UPLOAD_FOLDER, str(id))
    os.makedirs(demanda_folder, exist_ok=True)
    file.save(os.path.join(demanda_folder, filename))
    flash('Arquivo enviado com sucesso!')
    return redirect(url_for('demandas.ver_demanda', id=id))

@demandas_bp.route('/download/<int:id>/<path:nome_arquivo>')
@login_required
def download_arquivo(id, nome_arquivo):
    demanda_folder = os.path.join(UPLOAD_FOLDER, str(id))
    nome_arquivo = normalizar_nome(nome_arquivo)
    return send_from_directory(demanda_folder, nome_arquivo, as_attachment=True)

@demandas_bp.route('/excluir_arquivo/<int:id>/<path:nome_arquivo>', methods=['POST'])
@login_required
def excluir_arquivo(id, nome_arquivo):
    pasta = os.path.join(UPLOAD_FOLDER, str(id))
    nome_arquivo = normalizar_nome(nome_arquivo)
    caminho = os.path.join(pasta, nome_arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)
        flash('Arquivo excluído com sucesso.')
    else:
        flash('Arquivo não encontrado.')
    return redirect(url_for('demandas.ver_demanda', id=id))

@demandas_bp.route('/formulario')
def formulario_cliente():
    return render_template('formulario_cliente.html')

@demandas_bp.route('/submeter_demanda', methods=['POST'])
def submeter_demanda():
    dados = {campo: request.form.get(campo) for campo in [
        'nome', 'cpf', 'rg', 'endereco', 'email', 'telefone',
        'profissao', 'parte_contraria', 'objetivo', 'descricao', 'nome_empresa'
    ]}
    resposta_ia = gerar_resposta_ia(dados['descricao'])
    nova = Demanda(
        nome_cliente=dados['nome'],
        cpf=dados['cpf'],
        rg=dados['rg'],
        endereco=dados['endereco'],
        email=dados['email'],
        telefone=dados['telefone'],
        profissao=dados['profissao'],
        parte_contraria=dados['parte_contraria'],
        objetivo=dados['objetivo'],
        nome_empresa=dados['nome_empresa'],
        descricao=dados['descricao'],
        resposta_ia=resposta_ia,
        data_entrada=datetime.now(),
        fase_processual="Inicial"
    )
    db.session.add(nova)
    db.session.commit()
    return redirect(url_for('demandas.formulario_cliente', enviado=1))

@demandas_bp.route('/mover/<int:id>/<direcao>', methods=['POST'])
@login_required
def mover_demanda(id, direcao):
    demanda = Demanda.query.get_or_404(id)
    try:
        index = FASES.index(demanda.fase_processual)
        if direcao == 'direita' and index < len(FASES) - 1:
            demanda.fase_processual = FASES[index + 1]
        elif direcao == 'esquerda' and index > 0:
            demanda.fase_processual = FASES[index - 1]
        db.session.commit()
    except ValueError:
        pass
    return redirect(url_for('demandas.painel'))

@demandas_bp.route('/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_demanda(id):
    demanda = Demanda.query.get_or_404(id)
    db.session.delete(demanda)
    db.session.commit()
    flash('Demanda excluída com sucesso.')
    return redirect(url_for('demandas.painel'))
