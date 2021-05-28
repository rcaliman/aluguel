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
    if f.logado():
        if request.form:    #instancia a classe Cliente com os dados do formulario de form_clientes       
            try:
                cliente = Cliente   (
                                        request.form['id'],
                                        request.form['nome'],
                                        request.form['data_nasc'],
                                        request.form['ci'],
                                        request.form['cpf'],
                                        request.form['tel1'],
                                        request.form['tel2'],
                                    )
            except:
                cliente = Cliente   (
                                        '0', # se o formulario nao retorna o id significa novo cliente
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

        todos_clientes = Cliente.busca_todos()
        
        return render_template  (
                                    'clientes.html',
                                    todos_clientes = todos_clientes,
                                ) 
    else:
        return render_template('login.html')
    
@app.route('/editarcliente', methods=['GET'])
def editarcliente():
    if f.logado():
        id_cliente = f.extrai_id_da_url(request.url)
        
        if id_cliente == '00': # se a id for 00 o sistema vai abrir a tela de adicionar novo
            cliente = '00'
        else:
            cliente = Cliente.busca_cliente(id_cliente) # senao recebe o cliente escolhido do banco
            
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
    
@app.route('/editarimovel', methods=['GET'])
def editarimovel():
    if f.logado():
        id_imovel= f.extrai_id_da_url(request.url)
        
        if id_imovel== '00': # se a id for 00 o sistema vai abrir a tela de adicionar novo
            imovel = '00'
        else:
            imovel = Imovel.busca_imovel(id_imovel) # senao recebe o imovel escolhido do banco
            
        return render_template  (
                                    'form_imoveis.html',
                                    imovel = imovel
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