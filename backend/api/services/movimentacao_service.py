from ..models import movimentacao_model
from api import db

def cadastrar_movimentacao(movimentacao):
    movimentacao_bd = movimentacao_model.Movimentacao(descricao=movimentacao.descricao,
                                                      data=movimentacao.data,
                                                      categoria=movimentacao.categoria,
                                                      tipo=movimentacao.tipo,
                                                      valor=movimentacao.valor)
    db.session.add(movimentacao_bd)
    db.session.commit()
    return movimentacao_bd

def listar_movimentacoes():
    movimentacoes = movimentacao_model.Movimentacao.query.all()
    return movimentacoes

def listar_movimentacao_id(id):
    movimentacao = movimentacao_model.Movimentacao.query.filter_by(id=id).first()
    return movimentacao

def editar_movimentacao(movimentacao_bd, movimentacao_nova):
    movimentacao_bd.descricao = movimentacao_nova.descricao
    movimentacao_bd.data = movimentacao_nova.data
    movimentacao_bd.categoria = movimentacao_nova.categoria
    movimentacao_bd.tipo = movimentacao_nova.tipo
    movimentacao_bd.valor = movimentacao_nova.valor
    db.session.commit()

def remover_movimentacao(movimentacao):
    db.session.delete(movimentacao)
    db.session.commit()