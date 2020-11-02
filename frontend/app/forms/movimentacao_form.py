from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, FloatField
from wtforms.validators import DataRequired, Length


class MovimentacaoForm(FlaskForm):

    categorias_escolhas = [('alimentacao', 'Alimentação'),('educacao', 'Educação'),
                           ('lazer','Lazer'),('saude', 'Saúde'),('transporte','Transporte')]
    tipos_escolhas = [('pagar', 'A Pagar'), ('receber', 'A Receber')]

    descricao = StringField("descricao", validators=[Length(min=5, max=100),DataRequired()])
    data = DateField("data", validators=[DataRequired()], format='%d/%m/%Y')
    categoria = SelectField('categoria', choices=categorias_escolhas)
    tipo = SelectField('tipo', choices=tipos_escolhas)
    valor = FloatField("valor", validators=[DataRequired()])