⚖️ advpy – Inteligência Jurídica com IA (Google Gemini + Flask)

advpy é uma aplicação web que utiliza Inteligência Artificial para gerar documentos jurídicos personalizados, análises estratégicas e oportunidades de demanda a partir da descrição de casos.

O projeto integra a API Google Gemini para geração de conteúdo jurídico e interpretação estratégica, além do repositório oficial LexML para consulta de jurisprudência real.

Ideal para advogados, estudantes de Direito ou qualquer operador do Direito que busca agilidade, pesquisa automática e automação no pré-processamento de peças jurídicas.

🚀 Funcionalidades Principais

✅ Geração automática de conteúdo jurídico:

Resumo do caso

Pré-petição inicial personalizada (com dados como nome, CPF, endereço, profissão, etc.)

Doutrina e artigos jurídicos aplicáveis

Jurisprudência fictícia gerada por IA (verossímil)

Jurisprudência real sugerida pela IA (com número de processo, tribunal, ementa e link)

Jurisprudência oficial via API LexML

✅ Radar de oportunidades jurídicas:

Busca e análise de notícias recentes com potencial jurídico usando NewsAPI

Interpretação estratégica automática de cada notícia, indicando oportunidades de demandas, riscos legais e ações estratégicas para advogados

Exibição em cards no dashboard com título, resumo e análise estratégica

Atualização de notícias somente quando o usuário solicitar, evitando recarga automática

✅ Gestão de demandas:

Cada demanda cadastrada possui ID único e página dedicada

Visualização do histórico, arquivos anexados e fases processuais

Interface tipo CRM, permitindo movimentação lateral dos cards (fases processuais)

✅ Autenticação segura via JWT (JSON Web Token):

Implementação de login e controle de acesso usando tokens JWT

Proteção das rotas sensíveis da aplicação para usuários autenticados

Validação de tokens para manter sessões seguras e sem necessidade de estado no servidor

Facilita integração com frontends modernos e mobile apps mantendo segurança e escalabilidade

🧠 Tecnologias Utilizadas

Python 3.10+

Flask

Google Gemini – Geração de conteúdo jurídico e interpretação estratégica

LexML – Consulta pública de jurisprudência

NewsAPI – Coleta de notícias jurídicas

JSON Web Token (JWT) – Autenticação segura e stateless

HTML5 + CSS3 + Bootstrap (layout responsivo)

JavaScript (interatividade e manipulação de dashboard)

🖥️ Como Executar Localmente

Clone o repositório:

git clone https://github.com/seu-usuario/advpy.git
cd advpy


Crie e ative um ambiente virtual:

Linux/macOS:

python -m venv venv
source venv/bin/activate


Windows:

python -m venv venv
venv\Scripts\activate


Instale as dependências:

pip install -r requirements.txt


Crie o arquivo .env com suas chaves e configurações:

GEMINI_API_KEY=sua-chave-gemini
NEWSAPI_KEY=sua-chave-newsapi
JWT_SECRET_KEY=sua-chave-secreta-para-jwt


Execute a aplicação:

python app.py


Acesse no navegador:

http://127.0.0.1:5000

📁 Estrutura de Arquivos
advpy/
├── app.py                # Código principal Flask
├── noticias.py           # Módulo de notícias jurídicas e interpretação estratégica
├── auth.py               # Módulo para autenticação JWT (separado, se houver)
├── templates/
│   ├── formulario.html   # Página de entrada de dados
│   ├── resultado.html    # Exibe resultados gerados pela IA
│   ├── noticias.html     # Exibição de notícias e interpretação estratégica
│   ├── login.html        # Tela de login para autenticação
├── static/               # CSS, JS e assets
├── requirements.txt      # Dependências do projeto
├── .env                  # Contém suas chaves GEMINI_API_KEY, NEWSAPI_KEY e JWT_SECRET_KEY (não subir ao GitHub)
└── README.md             # Este arquivo

🔐 .env (Exemplo)
GEMINI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
NEWSAPI_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
JWT_SECRET_KEY=uma-chave-secreta-muito-segura

📦 requirements.txt (Exemplo)
flask
python-dotenv
requests
pyjwt

📝 Licença

Este projeto é livre para uso educacional e profissional. Licença personalizada pode ser adicionada conforme sua preferência.

Autor: Roque Rafael Proença
