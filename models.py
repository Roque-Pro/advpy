from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Demanda(db.Model):
    __tablename__ = 'demandas'

    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    rg = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    profissao = db.Column(db.String(50), nullable=False)
    nome_empresa = db.Column(db.String(100), nullable=True)
    parte_contraria = db.Column(db.String(100), nullable=False)
    objetivo = db.Column(db.Text, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    resposta_ia = db.Column(db.Text, nullable=True)
    data_entrada = db.Column(db.DateTime, nullable=False)
    fase_processual = db.Column(db.String(50), nullable=False)

    arquivos = db.relationship('Arquivo', backref='demanda', lazy=True)


class Arquivo(db.Model):
    __tablename__ = 'arquivos'

    id = db.Column(db.Integer, primary_key=True)
    nome_arquivo = db.Column(db.String(255), nullable=False)
    caminho = db.Column(db.String(255), nullable=False)
    demanda_id = db.Column(db.Integer, db.ForeignKey('demandas.id'), nullable=False)
