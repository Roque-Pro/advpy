from extensions import db

class Demanda(db.Model):
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

    
    


class Arquivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_arquivo = db.Column(db.String(255), nullable=False)
    caminho = db.Column(db.String(255), nullable=False)
    demanda_id = db.Column(db.Integer, db.ForeignKey('demanda.id'), nullable=False)

    demanda = db.relationship('Demanda', backref=db.backref('arquivos', lazy=True))

