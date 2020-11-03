class Movimentacao():
    def __init__(self, descricao, data, categoria, tipo, valor):
        self.__descricao = descricao
        self.__data = data
        self.__categoria = categoria
        self.__tipo = tipo
        self.__valor = valor

    def to_dict(self):
        return {
                    'descricao': self.__descricao,
                    'data': str( self.__data),
                    'categoria': self.__categoria,
                    'tipo': self.__tipo,
                    'valor': float(self.__valor)
                }

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor