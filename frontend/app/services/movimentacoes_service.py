import requests
baseUrl = 'http://127.0.0.1:3333/'
def listar_movimentacoes():
    endpoint = 'movimentacoes'
    resp = requests.get(f'{baseUrl}{endpoint}')
    return resp.json()

def criar_movimentacao( nova_movimentacao):
    endpoint = 'movimentacoes'
    resp = requests.post(f'{baseUrl}{endpoint}', json=nova_movimentacao.to_dict())
    return resp

def listar_movimentacao_id(id):
    endpoint = 'movimentacoes'
    resp = requests.get(f'{baseUrl}{endpoint}/{id}')
    return resp.json()

def editar_movimentacao(id, movimentacao_nova):
    endpoint = 'movimentacoes'
    resp = requests.put(f'{baseUrl}{endpoint}/{id}', json=movimentacao_nova.to_dict())
    return resp

def remover_movimentacao(id):
    endpoint = 'movimentacoes'
    requests.delete(f'{baseUrl}{endpoint}/{id}')