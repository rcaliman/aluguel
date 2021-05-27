from flask import Flask, session, request, render_template, redirect
from classe_usuario import Usuario
from classe_cliente import Cliente
from classe_imovel import Imovel
import funcoes_diversas as f

app = Flask(__name__)

app.secret_key = 'segredosecreto'

@app.route('/')
def inicio():
    if f.logado():
        return render_template('inicio.html')
    else:
        return render_template('login.html')  
    
@app.route('/clientes', methods=['POST','GET'])
def clientes():
    x = 'nao funcionou'
    if request.form:            
        cliente = Cliente   (
                                request.form['id'],
                                request.form['nome'],
                                request.form['data_nasc'],
                                request.form['ci'],
                                request.form['cpf'],
                                request.form['tel1'],
                                request.form['tel2'],
                            )
        try:  
            if request.form['apagar']:
                cliente.apagar()
        except:
            cliente.salvar()
        
    if f.logado():
        todos_clientes = Cliente.busca_todos()
        return render_template  (
                                    'clientes.html',
                                    todos_clientes = todos_clientes,
                                    x = x
                                ) 
    else:
        return render_template('login.html')
    
@app.route('/editarcliente', methods=['GET'])
def editarcliente():
    if f.logado():
        id_cliente = f.extrai_id_da_url(request.url)
        cliente = Cliente.busca_cliente(id_cliente)
        return render_template  (
                                    'form_clientes.html',
                                    cliente = cliente
                                )
    else:
        return render_template('login.html')

@app.route('/imoveis')
def imoveis():
    if f.logado():
        todos_imoveis = Imovel.busca_todos()
        return render_template  (
                                    'imoveis.html',
                                    todos_imoveis = todos_imoveis
                                )
    else:
        return render_template('login.html')

@app.route('/logar', methods=['POST'])
def logar():
    if Usuario.autenticacao(request.form['usuario'],request.form['senha']):
        session['usuario'] = request.form['usuario']
        return render_template('inicio.html')
    else:
        return render_template('login.html')

@app.route('/deslogar')
def deslogar():
    session.pop('usuario', default=None)
    return render_template('login.html')
    
app.run(debug=True)