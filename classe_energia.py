from classe_banco import UsaBanco
import parametros_banco

class Energia:
    def __init__(self, id, data, relogio1, relogio2, relogio3, valor_kwh, valor_conta):
        self.id = id
        self.data = data
        self.relogio1 = relogio1
        self.relogio2 = relogio2
        self.relogio3 = relogio3
        self.valor_kwh = valor_kwh if valor_kwh else 0
        self.valor_conta = valor_conta if valor_conta else 0

    def atualizar(self):
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""update al_energia set
                                data = '{self.data}',
                                relogio1 = '{self.relogio1}',
                                relogio2 = '{self.relogio2}',
                                relogio3 = '{self.relogio3}',
                                valor_kwh = '{self.valor_kwh}',
                                valor_conta = '{self.valor_conta}' 
                            where id = {self.id}"""
            cursor.execute(_SQL)

    def inserir(self):
        parametros = parametros_banco.parametros()
        if not self.data:
            self.data = '0000-00-00'
        with UsaBanco(parametros) as cursor:
            _SQL = f"""insert into al_energia
                (data, relogio1, relogio2, relogio3, valor_kwh, valor_conta) values (
                    '{self.data}',
                    '{self.relogio1}',
                    '{self.relogio2}',
                    '{self.relogio3}',
                    '{self.valor_kwh}',
                    '{self.valor_conta}');"""
            cursor.execute(_SQL) 

    def salvar(self):
        try:
            if int(self.id) > 0:
                self.atualizar()
            else:
                self.inserir()
        except:
            return 'erro'

    def apagar(self):
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""delete from al_energia where id={self.id};"""
            cursor.execute(_SQL)

    @staticmethod
    def busca_contas(limite):
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""SELECT * FROM (
                            SELECT * FROM al_energia ORDER BY id DESC LIMIT {limite}
                        ) sub
                            ORDER BY id ASC"""
            cursor.execute(_SQL)
            resultado = cursor.fetchall()
        return resultado  

    @staticmethod
    def busca_energia(id):
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""select * from al_energia where id =  {id};"""
            cursor.execute(_SQL)
            resultado = cursor.fetchall()
        return resultado
