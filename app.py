import os
import re
import requests
from flask import Flask, request, render_template
from groq import Groq
from dotenv import load_dotenv
from xml.etree import ElementTree as ET

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

app = Flask(__name__)


# Função para buscar jurisprudência real via LexML
def buscar_jurisprudencia_real(termo):
    try:
        url = "https://www.lexml.gov.br/busca/search"
        params = {
            "q": termo,
            "formato": "xml",
            "ordenar-por": "relevancia",
            "max": 3
        }
        response = requests.get(url, params=params)
        tree = ET.fromstring(response.content)

        resultados = []
        for item in tree.findall(".//registro"):
            titulo = item.findtext("titulo") or "Sem título"
            fonte = item.findtext("fonte") or "Fonte desconhecida"
            link = item.findtext("url") or "#"

            resultados.append(
                f"<strong>{titulo}</strong><br><em>{fonte}</em><br><a href='{link}' target='_blank'>Ver documento</a><br><br>"
            )

        return "".join(resultados) if resultados else "Nenhuma jurisprudência encontrada para este tema."

    except Exception as e:
        return f"Erro ao buscar jurisprudência: {str(e)}"


@app.route("/")
def formulario():
    return render_template("formulario.html")


@app.route("/processar", methods=["POST"])
def processar():
    # Coleta dos dados do formulário
    nome = request.form.get("nome", "")
    cpf = request.form.get("cpf", "")
    endereco = request.form.get("endereco", "")
    profissao = request.form.get("profissao", "")
    nome_empresa = request.form.get("nome_empresa", "")
    descricao = request.form.get("descricao", "")

    # Prompt enviado à IA
    prompt = f"""
A partir do texto abaixo, gere os seguintes elementos, cada um iniciado com ### e seu título:

1. Resumo do Caso (até 500 caracteres)
2. Pré-Petição Inicial (utilize variáveis como [NOME], [CPF], [ENDEREÇO], [PROFISSÃO], [EMPRESA])
3. Doutrina e Artigos Aplicáveis
4. Jurisprudência Fictícia (crie um exemplo fictício de jurisprudência, mesmo que inventado, mas verossímil)
5. Jurisprudência Real Sugerida pela IA

No item 5, forneça duas jurisprudências reais julgadas por tribunais brasileiros, cada uma contendo:

- Número do processo
- Tribunal
- Órgão julgador
- Data do julgamento
- Ementa
- Link para a decisão completa (se houver)

Inclua ao final de cada jurisprudência a linha: Fonte: [LINK]

Texto do caso: {descricao}
    """

    try:
        resposta = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        resposta_texto = resposta.choices[0].message.content
    except Exception as e:
        return render_template("resultado.html",
            resumo="",
            pre_peticao="",
            doutrina="",
            jurisprudencia_ficticia="",
            jurisprudencias_real_ia=[],
            jurisprudencia_real_web="",
            erro_ia=str(e)
        )

    # Dividir resposta em partes
    partes = resposta_texto.split("###")
    resumo = partes[1].strip() if len(partes) > 1 else ""
    pre_peticao_raw = partes[2].strip() if len(partes) > 2 else ""
    doutrina = partes[3].strip() if len(partes) > 3 else ""
    jurisprudencia_ficticia = partes[4].strip() if len(partes) > 4 else ""
    jurisprudencia_real_ia_texto = partes[5].strip() if len(partes) > 5 else ""

    # Substituir variáveis na pré-petição
    pre_peticao = (
        pre_peticao_raw.replace("[NOME]", nome)
                       .replace("[CPF]", cpf)
                       .replace("[ENDEREÇO]", endereco)
                       .replace("[PROFISSÃO]", profissao)
                       .replace("[EMPRESA]", nome_empresa)
    )

    # Extrair jurisprudências reais da IA com regex robusto
    matches = re.findall(r'(.*?)Fonte:\s*(https?://\S+)', jurisprudencia_real_ia_texto, re.DOTALL)
    jurisprudencias_real_ia = []
    for texto, fonte in matches:
        jurisprudencias_real_ia.append({
            "texto": texto.strip().replace('\n', '<br>'),
            "fonte": fonte.strip()
        })

    # Buscar jurisprudência real com LexML
    jurisprudencia_real_web = buscar_jurisprudencia_real(descricao)

    return render_template(
        "resultado.html",
        resumo=resumo,
        pre_peticao=pre_peticao,
        doutrina=doutrina,
        jurisprudencia_ficticia=jurisprudencia_ficticia,
        jurisprudencias_real_ia=jurisprudencias_real_ia,
        jurisprudencia_real_web=jurisprudencia_real_web
    )


if __name__ == "__main__":
    app.run(debug=True)
