from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from utils import login_required
import jwt
import datetime
import os
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

auth_bp = Blueprint('auth', __name__)

# Variáveis do .env
ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")

# 🔑 Gera token JWT com expiração de 1h
def gerar_token():
    payload = {
        "username": ADMIN_USER,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, current_app.config["JWT_SECRET_KEY"], algorithm="HS256")
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    token = session.get('token')

    # 🔁 Verifica se o token JWT é válido
    if token:
        try:
            jwt.decode(token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
            return redirect(url_for('demandas.painel'))
        except (ExpiredSignatureError, InvalidTokenError):
            session.clear()  # Token inválido ou expirado → limpa sessão

    # 📝 Processamento do formulário de login
    if request.method == 'POST':
        usuario = request.form.get('usuario', '')
        senha = request.form.get('senha', '')

        if usuario == ADMIN_USER and senha == ADMIN_PASS:
            session['logado'] = True
            session['usuario'] = ADMIN_USER
            session['token'] = gerar_token()
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
