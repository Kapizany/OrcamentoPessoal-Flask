import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dateutil.relativedelta import relativedelta
import matplotlib.style as style
style.use('ggplot')

class Graficos():

    def __init__(self, movimentacoes):
        movimentacoes_bd = pd.DataFrame(movimentacoes)
        movimentacoes_bd['data'] = pd.to_datetime(movimentacoes_bd['data'], format='%Y-%m-%d')
        movimentacoes_bd['mes'] = pd.DatetimeIndex(movimentacoes_bd['data']).month_name()
        months = {'January': 'Jan', 'February': 'Fev', 'March': 'Mar', 'April': 'Abr',
                       'May': 'Mai', 'June': 'Jun', 'July': 'Jul', 'August': 'Ago',
                       'September': 'Set', 'October': 'Out', 'November': 'Nov', 'December': 'Dez'}
        for month in months:
            movimentacoes_bd['mes'].replace(month, months[month], inplace=True)
        movimentacoes_bd['ano'] = pd.DatetimeIndex(movimentacoes_bd['data']).year
        movimentacoes_bd['ano'] = movimentacoes_bd.ano.apply(str)
        movimentacoes_bd['mes_ano'] = movimentacoes_bd['mes'] + '/' + movimentacoes_bd['ano']
        aux_date = max(movimentacoes_bd['data']) + relativedelta(months=-2)
        aux_mes = months[max(movimentacoes_bd['data']).month_name()]
        aux_ano = str(max(movimentacoes_bd['data']).year)
        self.aux_mes_ano = aux_mes + '/' + aux_ano
        min_date = pd.to_datetime(f'{aux_date.year}-{aux_date.month}-01')
        new_df = movimentacoes_bd[movimentacoes_bd['data'] >= min_date]
        self.descricao_df = new_df.groupby(['descricao', 'mes_ano']).sum().drop('id', axis=1).reset_index()
        self.mes_ano_df = new_df.groupby('mes_ano').sum().drop('id', axis=1).reset_index()

    def pie_chart(self,caminho):
        pie_data = self.descricao_df[self.descricao_df['mes_ano'] == self.aux_mes_ano]

        def func(pct, allvals):
            absolute = int(round(pct / 100. * np.sum(allvals)))
            return "{:.1f}%\n({:d} R$)".format(pct, absolute)

        fig1, ax1 = plt.subplots(figsize=(12, 8))

        wedges, texts, autotexts = ax1.pie(pie_data['valor'], autopct=lambda pct: func(pct, pie_data['valor']),
                                           textprops=dict(color="w"))

        ax1.legend(wedges, pie_data['descricao'],
                   title="Descrição",
                   loc="center left",
                   bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=10, weight="bold")

        plt.savefig(caminho)
        return self.aux_mes_ano

    def bar_chart(self, caminho):
        fig, ax1 = plt.subplots(figsize=(12, 8))
        figure = plt.bar(self.mes_ano_df['mes_ano'], self.mes_ano_df['valor'])
        figure[0].set_color('r')
        figure[1].set_color('b')
        figure[2].set_color('y')
        plt.savefig(caminho)