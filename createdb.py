from extensions import db
from models import Demanda, Arquivo  # Isso parece estar certo
from main import app  # Corrigido aqui

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso.")
