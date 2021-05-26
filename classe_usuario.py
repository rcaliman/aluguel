from classe_banco import UsaBanco
import parametros_banco

class Usuario:
    def __init__(self, id, nome, usuario, senha, email, grupo):
        self.id = id
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        self.email = email
        self.grupo = grupo
    
    
    @staticmethod
    def autenticacao(usuario, senha):
        parametros = parametros_banco.parametros()
        with UsaBanco(parametros) as cursor:
            _SQL = f"""select * from al_usuarios where usuario = '{usuario}' and senha = '{senha}';"""
            cursor.execute(_SQL)
            resultado = cursor.fetchall()
        if resultado:
            return usuario