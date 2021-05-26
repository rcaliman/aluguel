from classe_banco import UsaBanco
import parametros_banco

class Cliente:
    def __init__(self, nome, data_nasc, ci, cpf, tel1, tel2):
        self.nome = nome
        self.data_nasc = data_nasc
        self.ci = ci
        self.cpf = cpf
        self.tel1 = tel1
        self.tel2 = tel2
        
    @staticmethod
    def busca_cliente(id):
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""select * from al_clientes where id = {id};"""
            cursor.execute(_SQL)
            return cursor.fetchall()
            
     
    @staticmethod
    def busca_todos():
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = """select * from al_clientes;"""
            cursor.execute(_SQL)
            resultado = cursor.fetchall()
        return resultado    
        