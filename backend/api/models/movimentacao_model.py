from api import db

class Movimentacao(db.Model):
    __tablename__ = 'movimentacoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, nullable=False)
    categoria = db.Column(db.Enum("alimentacao", "educacao", "lazer", "saude", "transporte"), nullable=False)
    tipo = db.Column(db.Enum("pagar", "receber"), nullable=False)
    valor = db.Column(db.Float, nullable=False)