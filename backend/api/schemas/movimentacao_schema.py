from api import ma
from ..models import movimentacao_model
from marshmallow import fields

class MovimentacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = movimentacao_model.Movimentacao
        fields = ("id", "descricao", "data", "categoria", "tipo", "valor")
    descricao = fields.String(required=True)
    data = fields.Date(required=True)
    categoria = fields.String(required=True)
    tipo = fields.String(required=True)
    valor = fields.Float(required=True)