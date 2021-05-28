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
            
    
    def atualizar(self):
        """atualiza dados de um cliente"""
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
                
    def inserir(self):
        """insere um novo cliente"""
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""insert into al_clientes(nome, data_nasc, ci, cpf, tel1, tel2) values (
                '{self.nome}','{self.data_nasc}','{self.ci}','{self.cpf}','{self.tel1}','{self.tel2}');"""
            cursor.execute(_SQL) 
    
    def salvar(self):
        """descobre se os dados sao atualizacao de um cliente existente ou adicao de um novo cliente
        e chama o metodo que executa a acao"""
        if int(self.id) > 0:
            self.atualizar()
        else:
            self.inserir()          
                
    def apagar(self):
        """apaga um cliente do banco"""
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""delete from al_clientes where id={self.id};"""
            cursor.execute(_SQL)
            
    @staticmethod
    def busca_cliente(id):
        """busca um cliente no banco"""
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""select * from al_clientes where id = {id};"""
            cursor.execute(_SQL)
            return cursor.fetchall()
            
     
    @staticmethod
    def busca_todos():
        """busca todos os clientes do banco"""
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = """select * from al_clientes order by nome;"""
            cursor.execute(_SQL)
            resultado = cursor.fetchall()
        return resultado    
        