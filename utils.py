import unicodedata
import requests
from werkzeug.utils import secure_filename
from flask import session, flash, redirect, url_for
from functools import wraps
from config import GEMINI_API_KEY

try:
    import markdown as md
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False

def normalizar_nome(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    return secure_filename(nome)

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('logado'):
            flash('Por favor, faça login para acessar essa página.')
            return redirect(url_for('auth.login'))
        return fn(*args, **kwargs)
    return wrapper

def gerar_resposta_ia(descricao):
    prompt = f"""
    Considere o seguinte relato do cliente sobre um caso jurídico. Com base nele...
    Relato do cliente:
    {descricao}
    """

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(url, headers=headers, params=params, json=data, timeout=30)
        resposta_json = response.json()
        texto = resposta_json['candidates'][0]['content']['parts'][0]['text']

        if HAS_MARKDOWN:
            try:
                return md.markdown(texto, extensions=['fenced_code', 'tables'])
            except Exception:
                return texto
        return texto
    except Exception as e:
        print("Erro IA:", e)
        return "Erro ao obter resposta da IA."
