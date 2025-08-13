from extensions import db
from models import Demanda, Arquivo  # ou o nome correto do seu arquivo de modelos
from app import app  # ou o nome da sua instância Flask

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso.")
