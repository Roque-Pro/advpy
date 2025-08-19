from config import create_app
from auth import auth_bp
from demandas import demandas_bp
from noticias import bp_noticias
from extensions import db

app = create_app()

# ✅ Registro de blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(demandas_bp)
app.register_blueprint(bp_noticias)

# 🔧 Inicialização do banco (somente para dev/local)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Evite em produção, use migrations
    app.run(debug=True)
