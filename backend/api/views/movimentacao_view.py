from flask_restful import Resource
from api import api
from ..schemas import movimentacao_schema
from flask import request, make_response, jsonify
from ..entidades import movimentacao
from ..services import movimentacao_service


class MovimentacaoList(Resource):
    def get(self):
        movimentacoes = movimentacao_service.listar_movimentacoes()
        ts = movimentacao_schema.MovimentacaoSchema(many=True)
        return make_response(ts.jsonify(movimentacoes), 200)

    def post(self):
        ts = movimentacao_schema.MovimentacaoSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            descricao = request.json["descricao"]
            data = request.json["data"]
            categoria = request.json["categoria"]
            tipo = request.json["tipo"]
            valor = request.json["valor"]
            nova_movimentacao = movimentacao.Movimentacao(descricao=descricao,
                                                          data=data, categoria=categoria,
                                                          tipo=tipo, valor=valor)
            result = movimentacao_service.cadastrar_movimentacao(nova_movimentacao)
            return make_response(ts.jsonify(result), 201)

class MovimentacaoDetail(Resource):
    def get(self, id):
        movimentacao_bd = movimentacao_service.listar_movimentacao_id(id)
        if movimentacao_bd is None:
            return make_response(jsonify("Movimentação não encontrada"), 404)
        else:
            ts = movimentacao_schema.MovimentacaoSchema()
            return make_response(ts.jsonify(movimentacao_bd), 200)

    def put(self, id):
        movimentacao_bd = movimentacao_service.listar_movimentacao_id(id)
        if movimentacao_bd is None:
            return make_response(jsonify("Movimentação não encontrada"), 404)
        ts = movimentacao_schema.MovimentacaoSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            descricao = request.json["descricao"]
            data = request.json["data"]
            categoria = request.json["categoria"]
            tipo = request.json["tipo"]
            valor = request.json["valor"]
            nova_movimentacao = movimentacao.Movimentacao(descricao=descricao,
                                                          data=data, categoria=categoria,
                                                          tipo=tipo, valor=valor)
            movimentacao_service.editar_movimentacao(movimentacao_bd=movimentacao_bd,
                                                     movimentacao_nova=nova_movimentacao)
            movimentacao_atualizada = movimentacao_service.listar_movimentacao_id(id)
            return make_response(ts.jsonify(movimentacao_atualizada), 200)
    def delete(self, id):
        movimentacao_bd = movimentacao_service.listar_movimentacao_id(id)
        if movimentacao_bd is None:
            return make_response(jsonify("Movimentação não encontrada"), 404)
        movimentacao_service.remover_movimentacao(movimentacao_bd)
        return make_response('', 200)

api.add_resource(MovimentacaoList, '/movimentacoes')
api.add_resource(MovimentacaoDetail, '/movimentacoes/<int:id>')