import unicodedata
import requests
from werkzeug.utils import secure_filename
from flask import session, flash, redirect, url_for, request, jsonify, current_app
from functools import wraps
import jwt

from config import GEMINI_API_KEY

try:
    import markdown as md
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False

def normalizar_nome(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    return secure_filename(nome)

def gerar_resposta_ia(descricao):
    prompt = f"""
    Considere o seguinte relato de um cliente sobre um caso jurídico. Com base nele, gere um resumo do caso com até 200 palavras, uma pré-petição inicial com campos específicos de substituição (como [NOME DO CLIENTE], [NOME DO RÉU], [VALOR], etc.), as leis aplicáveis, jurisprudência relevante relacionada e uma opinião geral sobre o caso.

    Relato do cliente:
    {descricao}

    Exemplo de resposta esperada:
    - Resumo do Caso (200 palavras):
    - Pré-Petição Inicial: 
      [modelo de petição com campos em colchetes]
    - Leis Aplicáveis:
    - Jurisprudência real de caso semelhante ou parecido:
    - Opinião da IA:
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

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None

        # Primeiro tenta buscar da session (usado em navegação normal)
        if session.get("token"):
            token = session["token"]

        # Depois tenta pelo header Authorization (usado em APIs)
        elif "Authorization" in request.headers:
            auth_header = request.headers.get("Authorization")
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            if request.path.startswith("/api/"):
                return jsonify({"error": "Token JWT não fornecido."}), 401
            flash("Você precisa estar logado para acessar esta página.")
            return redirect(url_for("auth.login"))

        try:
            payload = jwt.decode(token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            if request.path.startswith("/api/"):
                return jsonify({"error": "Token expirado."}), 401
            flash("Sua sessão expirou. Faça login novamente.")
            return redirect(url_for("auth.login"))
        except jwt.InvalidTokenError:
            if request.path.startswith("/api/"):
                return jsonify({"error": "Token inválido."}), 401
            flash("Token inválido. Faça login novamente.")
            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)

    return decorated_function
