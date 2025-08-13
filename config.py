import os
import secrets
from dotenv import load_dotenv
from flask import Flask
from extensions import db

load_dotenv()

# Variáveis do .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "senha123")
APP_SECRET = os.getenv("APP_SECRET_KEY") or secrets.token_hex(16)

# Pasta de uploads
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = APP_SECRET

    db.init_app(app)
    return app
