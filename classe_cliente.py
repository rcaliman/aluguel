from classe_banco import UsaBanco
import parametros_banco

class Cliente:
    def __init__(self, id, nome, data_nasc, ci, cpf, tel1, tel2):
        self.id = id
        self.nome = nome
        self.data_nasc = data_nasc
        self.ci = ci
        self.cpf = cpf
        self.tel1 = tel1
        self.tel2 = tel2
    
    def salvar(self):
        if int(self.id) > 0:
            parametros = parametros_banco.parametros()
            with UsaBanco(parametros) as cursor:
                _SQL = f"""update al_clientes set
                                nome = '{self.nome}',
                                data_nasc = '{self.data_nasc}',
                                ci = '{self.ci}',
                                cpf = '{self.cpf}',
                                tel1 = '{self.tel1}',
                                tel2 = '{self.tel2}' 
                            where id = {self.id}"""
                cursor.execute(_SQL)
    def apagar(self):
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""delete from al_clientes where id={self.id};"""
            cursor.execute(_SQL)
            
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
            _SQL = """select * from al_clientes order by nome;"""
            cursor.execute(_SQL)
            resultado = cursor.fetchall()
        return resultado    
        