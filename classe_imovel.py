from classe_banco import UsaBanco
import parametros_banco

class Imovel:
    def __init__(self, id, tipo, numero, local, cliente, valor_aluguel, observacao, dia_base):
        self.id = id
        self.tipo = tipo
        self.numero = numero
        self.local = local
        self.cliente = cliente
        self.valor_aluguel = float(valor_aluguel)
        self.observacao = observacao
        self.dia_base = dia_base
    
    def atualizar(self):
        """atualiza dados de um imovel"""
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""update al_imoveis set
                                tipo = '{self.tipo}',
                                numero = '{self.numero}',
                                local = '{self.local}',
                                cliente = '{self.cliente}',
                                valor_aluguel = '{self.valor_aluguel}',
                                observacao = '{self.observacao}',
                                dia_base = '{self.dia_base}'
                            where id = {self.id}"""
            cursor.execute(_SQL)
                
    def inserir(self):
        """insere um novo imovel"""
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""insert into al_imoveis
                (tipo, numero, local, cliente, valor_aluguel, observacao, dia_base) values (
                    '{self.tipo}',
                    '{self.numero}',
                    '{self.local}',
                    '{self.cliente}',
                    '{self.valor_aluguel}',
                    '{self.observacao}',
                    '{self.dia_base}');"""
            cursor.execute(_SQL) 
    
    def salvar(self):
        """descobre se os dados sao atualizacao de um imovel existente ou adicao de um novo imovel
        e chama o metodo que executa a acao"""
        if int(self.id) > 0:
            self.atualizar()
        else:
            self.inserir()  
    
    def apagar(self):
        """apaga um imovel do banco"""
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""delete from al_imoveis where id={self.id};"""
            cursor.execute(_SQL)
    
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
        