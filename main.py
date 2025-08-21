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
    with app.app_context():
        from extensions import db
        db.create_all()
    app.run(debug=True)
