from flask import render_template, redirect, url_for
from app import app

from app.forms import movimentacao_form
from app.entidades import movimentacao
from app.services import movimentacoes_service
from app.utils import graficos

@app.route("/home", methods=["GET", "POST"])
def home():
    form = movimentacao_form.MovimentacaoForm()
    movimentacoes_bd = movimentacoes_service.listar_movimentacoes()
    if form.validate_on_submit():
        descricao = form.descricao.data
        data = form.data.data
        categoria = form.categoria.data
        tipo = form.tipo.data
        valor = form.valor.data

        nova_movimentacao = movimentacao.Movimentacao(descricao=descricao, data=data, categoria=categoria,
                                                      tipo=tipo, valor=valor)
        try:
            movimentacoes_service.criar_movimentacao(nova_movimentacao)
            return redirect(url_for("home"))
        except:
            print("Cliente não cadastrado")

    return render_template('home.html', form_template=form, movimentacoes=movimentacoes_bd)

@app.route("/movimentacoes", methods=["GET"])
def movimentacoes():
    movimentacoes_bd = movimentacoes_service.listar_movimentacoes()
    return render_template('movimentacoes.html', movimentacoes=movimentacoes_bd)

@app.route("/movimentacoes/<id>", methods=["GET"])
def deletar_movimentacao(id):
    movimentacoes_service.remover_movimentacao(id)
    return redirect(url_for("movimentacoes"))

@app.route("/estatisticas", methods=["GET"])
def estatisticas():
    movimentacoes_bd = movimentacoes_service.listar_movimentacoes()
    graph_service = graficos.Graficos(movimentacoes_bd)
    caminho_bar = 'app/static/css/images/new_bar_plot.png'
    caminho_pie = 'app/static/css/images/new_pie_plot.png'
    graph_service.bar_chart(caminho_bar)
    mes_ano = graph_service.pie_chart(caminho_pie)
    return render_template('estatisticas.html', mes_ano=mes_ano)