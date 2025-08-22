import os
from config import create_app
from auth import auth_bp
from demandas import demandas_bp
from noticias import bp_noticias
# from noticias import noticias_bp  # vamos criar depois

app = create_app()

app.register_blueprint(auth_bp)
app.register_blueprint(demandas_bp)
app.register_blueprint(bp_noticias)
# app.register_blueprint(noticias_bp)

if __name__ == '__main__':
    # Pega a variável de ambiente 'PORT', que o Render define automaticamente
    port = int(os.environ.get('PORT', 5000))  # Se não encontrar, usa a porta 5000
    # Executa o Flask na porta correta e com o host 0.0.0.0 para ser acessível externamente
    app.run(debug=True, host='0.0.0.0', port=port)
