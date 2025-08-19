from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify, current_app
from utils import login_required
import jwt
import datetime
import os

auth_bp = Blueprint('auth', __name__)

# Variáveis do .env
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "senha123")

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

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logado') and session.get('token'):
        return redirect(url_for('demandas.painel'))

    erro = None
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

# 🔹 Rota de API opcional para login via JSON
@auth_bp.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    usuario = data.get("usuario")
    senha = data.get("senha")

    if usuario == ADMIN_USER and senha == ADMIN_PASS:
        token = gerar_token()
        return jsonify({"token": token, "user": {"username": ADMIN_USER}}), 200

    return jsonify({"error": "Credenciais inválidas"}), 401
