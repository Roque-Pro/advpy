import requests
from flask import Blueprint, render_template
import os
import json
from utils import login_required  # importei o decorator

bp_noticias = Blueprint("noticias", __name__)

ULTIMAS_NOTICIAS = []

# Chaves do .env
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def gerar_interpretacao_ia(titulo, descricao, fonte):
    prompt = f"""
    Você é um assistente jurídico. Analise a seguinte notícia e gere uma interpretação estratégica para advogados, mostrando possíveis oportunidades de demanda, ações estratégicas ou insights jurídicos:

    Título: {titulo}
    Descrição: {descricao}
    Fonte: {fonte}

    Responda em texto curto (2-3 frases) destacando oportunidades jurídicas.
    """
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {"contents":[{"parts":[{"text": prompt}]}]}

    try:
        response = requests.post(url, headers=headers, params=params, json=data, timeout=20)
        texto = response.json()['candidates'][0]['content']['parts'][0]['text']
        return texto.strip()
    except Exception as e:
        print("Erro ao gerar interpretação IA:", e)
        return "Não foi possível gerar interpretação estratégica."

def buscar_noticias():
    global ULTIMAS_NOTICIAS
    noticias = []

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "direito OR advogado OR justiça OR legislação OR tribunais",
        "language": "pt",
        "pageSize": 10,
        "sortBy": "publishedAt",
        "apiKey": NEWSAPI_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        for item in data.get("articles", []):
            titulo = item.get("title", "")
            descricao = item.get("description", "")
            fonte = item.get("source", {}).get("name", "")

            interpretacao = gerar_interpretacao_ia(titulo, descricao, fonte)

            noticia = {
                "titulo": titulo,
                "descricao": descricao,
                "link": item.get("url", ""),
                "fonte": fonte,
                "interpretacao_estrategica": interpretacao
            }
            noticias.append(noticia)

        ULTIMAS_NOTICIAS = noticias
        return noticias

    except Exception as e:
        print("Erro ao buscar notícias:", e)
        return []

@bp_noticias.route("/noticias")
@login_required
def exibir_noticias():
    global ULTIMAS_NOTICIAS
    return render_template("noticias.html", noticias=ULTIMAS_NOTICIAS)

@bp_noticias.route("/noticias/atualizar")
@login_required
def atualizar_noticias():
    global ULTIMAS_NOTICIAS
    noticias = buscar_noticias()
    if noticias:
        ULTIMAS_NOTICIAS = noticias
    return render_template("noticias.html", noticias=ULTIMAS_NOTICIAS)
