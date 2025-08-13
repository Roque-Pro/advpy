from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from config import ADMIN_USER, ADMIN_PASS
from utils import login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logado'):
        return redirect(url_for('demandas.painel'))

    erro = None
    if request.method == 'POST':
        usuario = request.form.get('usuario', '')
        senha = request.form.get('senha', '')
        if usuario == ADMIN_USER and senha == ADMIN_PASS:
            session['logado'] = True
            session['usuario'] = usuario
            flash('Login realizado com sucesso.')
            return redirect(url_for('demandas.painel'))
        else:
            erro = "Usuário ou senha inválidos."
    return render_template('login.html', erro=erro)

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Você foi desconectado.')
    return redirect(url_for('auth.login'))
