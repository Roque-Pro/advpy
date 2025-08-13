# ⚖️ advpy – Inteligência Jurídica com IA (Google Gemini + Flask + LexML)

**advpy** é uma aplicação web que utiliza **Inteligência Artificial** para gerar documentos jurídicos personalizados, análises estratégicas e oportunidades de demanda a partir da descrição de casos.  

O projeto integra a **API Google Gemini** para geração de conteúdo jurídico e interpretação estratégica, além do repositório oficial **LexML** para consulta de jurisprudência real.

Ideal para **advogados**, **estudantes de Direito** ou qualquer operador do Direito que busca **agilidade**, **pesquisa automática** e **automação no pré-processamento de peças jurídicas**.

---

## 🚀 Funcionalidades Principais

✅ **Geração automática de conteúdo jurídico:**

- Resumo do caso
- Pré-petição inicial personalizada (com dados como nome, CPF, endereço, profissão, etc.)
- Doutrina e artigos jurídicos aplicáveis
- Jurisprudência fictícia gerada por IA (verossímil)
- Jurisprudência real sugerida pela IA (com número de processo, tribunal, ementa e link)
- Jurisprudência oficial via API LexML

✅ **Radar de oportunidades jurídicas:**

- Busca e análise de **notícias recentes com potencial jurídico** usando NewsAPI
- Interpretação estratégica automática de cada notícia, indicando oportunidades de demandas, riscos legais e ações estratégicas para advogados
- Exibição em **cards no dashboard** com título, resumo e análise estratégica
- Atualização de notícias **somente quando o usuário solicitar**, evitando recarga automática

✅ **Gestão de demandas:**

- Cada demanda cadastrada possui **ID único** e página dedicada
- Visualização do histórico, arquivos anexados e fases processuais
- Interface tipo CRM, permitindo movimentação lateral dos cards (fases processuais)

---

## 🧠 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Google Gemini](https://developers.generativeai.google/) – Geração de conteúdo jurídico e interpretação estratégica
- [LexML](https://www.lexml.gov.br/) – Consulta pública de jurisprudência
- [NewsAPI](https://newsapi.org/) – Coleta de notícias jurídicas
- HTML5 + CSS3 + Bootstrap (layout responsivo)
- JavaScript (interatividade e manipulação de dashboard)

---

## 🖥️ Como Executar Localmente

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/advpy.git
   cd advpy
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Crie o arquivo .env com suas chaves:

env
Copiar
Editar
GEMINI_API_KEY=sua-chave-gemini
NEWSAPI_KEY=sua-chave-newsapi
Execute a aplicação:

bash
Copiar
Editar
python app.py
Acesse no navegador:

cpp
Copiar
Editar
http://127.0.0.1:5000
📁 Estrutura de Arquivos
bash
Copiar
Editar
advpy/
├── app.py                  # Código principal Flask
├── noticias.py             # Módulo de notícias jurídicas e interpretação estratégica
├── templates/
│   ├── formulario.html     # Página de entrada de dados
│   ├── resultado.html      # Exibe resultados gerados pela IA
│   └── noticias.html       # Exibição de notícias e interpretação estratégica
├── static/                 # CSS, JS e assets
├── requirements.txt        # Dependências do projeto
├── .env                    # Contém suas chaves GEMINI_API_KEY e NEWSAPI_KEY (não subir ao GitHub)
└── README.md               # Este arquivo
🔐 .env (Exemplo)
env
Copiar
Editar
GEMINI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
NEWSAPI_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
📦 requirements.txt (Exemplo)
nginx
Copiar
Editar
flask
python-dotenv
requests
Adicione outras dependências que seu projeto usar (ex.: pandas, sqlalchemy etc.)

📝 Licença
Este projeto é livre para uso educacional e profissional.
Licença personalizada pode ser adicionada conforme sua preferência.

Autor
Roque Rafael Proença
