# ⚖️ advpy – Inteligência Jurídica com IA (Groq + Flask + LexML)

**advpy** é uma aplicação web que utiliza **Inteligência Artificial** para gerar documentos jurídicos personalizados com base na descrição de um caso, incluindo **petições iniciais**, **doutrina aplicável** e **jurisprudências reais**, integrando a **API Groq (LLaMA3-70B)** e o repositório oficial **LexML**.

Ideal para **advogados**, **estudantes de Direito** ou qualquer operador do Direito que busca agilidade, pesquisa e automação no pré-processamento de peças jurídicas.

---

## 🚀 Funcionalidades

✅ Geração automática de:

- ✅ **Resumo do caso**
- ✅ **Pré-petição personalizada** (com dados como nome, CPF, endereço, etc.)
- ✅ **Doutrina e artigos jurídicos aplicáveis**
- ✅ **Jurisprudência fictícia** (verossímil, gerada por IA)
- ✅ **Jurisprudência real sugerida pela IA** (com número de processo, tribunal, ementa e link)
- ✅ **Jurisprudência real oficial via API LexML**

---

## 🧠 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Groq API (LLaMA3-70B)](https://console.groq.com/)
- [LexML](https://www.lexml.gov.br/) – Consulta pública de jurisprudência
- HTML5 + CSS3 (layout simples e responsivo)

---


## 2 - Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

## 3 - Instale as dependências:

pip install -r requirements.txt

## 4 - Crie o arquivo .env com sua chave da Groq:

GROQ_API_KEY=sua-chave-groq-aqui

## 5 - Execute a aplicação:

python app.py

## 6 - Acesse no navegador:

    http://127.0.0.1:5000

## 📁 Estrutura de Arquivos

advpy/
├── app.py                  # Código principal Flask
├── templates/
│   ├── formulario.html     # Página de entrada de dados
│   └── resultado.html      # Exibe o resultado gerado
├── requirements.txt        # Dependências do projeto
├── .env                    # Contém sua chave GROQ_API_KEY (não subir ao GitHub)
└── README.md               # Este arquivo

## 🔐 .env (Exemplo)

Crie um arquivo .env na raiz do projeto com:

GROQ_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX

## 📦 requirements.txt (Exemplo)

flask
python-dotenv
groq
requests

## 📝 Licença

Este projeto é livre para uso educacional e profissional. Licença personalizada pode ser adicionada conforme sua preferência.


## Autor: Roque Rafael Proença

## 🖥️ Como Executar Localmente

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/advpy.git
   cd advpy
