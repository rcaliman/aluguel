from classe_banco import UsaBanco
import parametros_banco

class Imovel:
    def __init__(self, id, tipo, numero, local, cliente, valor_aluguel, observacao, dia_base):
        self.id = id
        self.tipo = tipo
        self.numero = numero
        self.local = local
        self.cliente = cliente
        self.valor_aluguel = valor_aluguel
        self.observacao = observacao
        self.dia_base = dia_base
        
    @staticmethod
    def busca_imovel(id):
        """busca um imovel no banco"""
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""select * from al_imoveis where id = {id};"""
            cursor.execute(_SQL)
            return cursor.fetchall()
        
    @staticmethod    
    def busca_todos():
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = """select * from al_imoveis;"""
            cursor.execute(_SQL)
            resultado = cursor.fetchall()
        return resultado
        