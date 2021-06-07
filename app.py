from flask import Flask, session, request, render_template, redirect
from classe_usuario import Usuario
from classe_cliente import Cliente
from classe_imovel import Imovel
from classe_energia import Energia
import numero_por_extenso
import utilitarios as u

app = Flask(__name__)

app.secret_key = 'segredosecreto'

@app.route('/')
def inicio():
    if u.MinhaUrl.logado():
        return render_template('inicio.html')
    else:
        return render_template('login.html')  

    
@app.route('/clientes', methods=['POST','GET'])
def clientes():
    url = u.MinhaUrl(request.url)
    if u.MinhaUrl.logado():          
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
        try:
            ordenador = url.acao()
        except:
            ordenador = 'nome'

        todos_clientes = Cliente.busca_todos(ordenador)
        
        return render_template  (
                                    'clientes.html',
                                    todos_clientes = todos_clientes,
                                ) 
    else:
        return render_template('login.html')

    
@app.route('/editarcliente', methods=['GET'])
def editarcliente():
    if u.MinhaUrl.logado():
        url = u.MinhaUrl(request.url)
        id_cliente = url.id()
        
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


@app.route('/imoveis', methods=['POST','GET'])
def imoveis():
    url = u.MinhaUrl(request.url)
    if u.MinhaUrl.logado():
        if request.form:    #instancia a classe Cliente com os dados do formulario de form_clientes       
            try:
                imovel = Imovel   (
                                        request.form['id'],
                                        request.form['tipo'],
                                        request.form['numero'],
                                        request.form['localizacao'],
                                        request.form['nome'],
                                        u.virgula_para_ponto(request.form['valor']),
                                        request.form['observacao'],
                                        request.form['dia_base'],
                                    )
            except:
                imovel = Imovel   (
                                        '0', # se o formulario nao retorna o id significa novo cliente
                                        request.form['tipo'],
                                        request.form['numero'],
                                        request.form['localizacao'],
                                        request.form['nome'],
                                        u.virgula_para_ponto(request.form['valor']),
                                        request.form['observacao'],
                                        request.form['dia_base'],
                                    )
            try:  
                if request.form['apagar']:
                    imovel.apagar()
            except:
                imovel.salvar() 
        try:
            ordenador = url.acao()
        except:
            ordenador = 'cliente'

        todos_imoveis = Imovel.busca_todos(ordenador)
        return render_template  (
                                    'imoveis.html',
                                    todos_imoveis = todos_imoveis,
                                    input_mes = u.input_mes(),
                                    input_ano = u.input_ano(),
                                )
    else:
        return render_template('login.html')

    
@app.route('/editarimovel', methods=['GET'])
def editarimovel():
    if u.MinhaUrl.logado():
        url = u.MinhaUrl(request.url)
        id_imovel= url.id()
        
        if id_imovel== '00': # se a id for 00 o sistema vai abrir a tela de adicionar novo
            imovel = '00'
        else:
            imovel = Imovel.busca_imovel(id_imovel) # senao recebe o imovel escolhido do banco
            
        return render_template  (
                                    'form_imoveis.html',
                                    imovel = imovel,
                                    input_select_clientes = Cliente.input_select_clientes(),
                                )
    else:
        return render_template('login.html')

@app.route('/recibos', methods=['POST'])
def recibos():
    ids = request.form.to_dict()
    mes = ids.pop('mes')
    ano = ids.pop('ano')
    lista_de_id= []
    for a in ids:
        lista_de_id.append(ids[a]) 
    
    dados_recibos = Imovel.busca_por_ids(lista_de_id)
    return render_template('recibos.html',
                    dados_recibos = dados_recibos,
                    extenso = numero_por_extenso.monetario,
                    telefones = Cliente.seleciona_telefones,
                    mes = mes,
                    ano = ano,
                    len = len,
                    str = str
                    )


@app.route('/energia', methods=['POST','GET'])
def energia():
    if u.MinhaUrl.logado():
        if request.form:    #instancia a classe Cliente com os dados do formulario de form_clientes       
            try:
                energia = Energia   (
                                        request.form['id'],
                                        request.form['data'],
                                        request.form['relogio1'],
                                        request.form['relogio2'],
                                        request.form['relogio3'],
                                        u.virgula_para_ponto(request.form['valor_kwh']),
                                        u.virgula_para_ponto(request.form['valor_conta']),
                                    )
            except:
                energia = Energia  (
                                        '0', # se o formulario nao retorna o id significa novo cliente
                                        request.form['data'],
                                        request.form['relogio1'],
                                        request.form['relogio2'],
                                        request.form['relogio3'],
                                        u.virgula_para_ponto(request.form['valor_kwh']),
                                        u.virgula_para_ponto(request.form['valor_conta']),
                                    )
            try:  
                if request.form['apagar']:
                    energia.apagar()
            except:
                energia.salvar() 
        
        busca_contas = u.busca_contas()
        
        if busca_contas[1][6] > 0:
            mes1total = busca_contas[1][6]
            mes1ktn1 = u.ponto_para_virgula(busca_contas[1][7] / busca_contas[1][10] * float(busca_contas[1][6]))
            mes1ktn2 = u.ponto_para_virgula(busca_contas[1][8] / busca_contas[1][10] * float(busca_contas[1][6]))
            mes1ktn3 = u.ponto_para_virgula(busca_contas[1][9] / busca_contas[1][10] * float(busca_contas[1][6]))
            mes1total = u.ponto_para_virgula(mes1total)
        else:
            mes1total = mes1ktn1 = mes1ktn2 = mes1ktn3 = 0
            
        mes1kwh = str(busca_contas[1][5]).replace('.',',')
        
        if busca_contas[2][6] > 0:
            mes2total = busca_contas[2][6]
            mes2ktn1 = u.ponto_para_virgula(busca_contas[2][7] / busca_contas[2][10] * float(busca_contas[2][6]))
            mes2ktn2 = u.ponto_para_virgula(busca_contas[2][8] / busca_contas[2][10] * float(busca_contas[2][6]))
            mes2ktn3 = u.ponto_para_virgula(busca_contas[2][9] / busca_contas[2][10] * float(busca_contas[2][6]))
            mes2total = u.ponto_para_virgula(mes2total)
        else:
            mes2total = mes2ktn1 = mes2ktn2 = mes2ktn3 = 0    
        
        mes2kwh = str(busca_contas[2][5]).replace('.',',')
        
        if busca_contas[3][6] > 0:
            mes3total = busca_contas[3][6]
            mes3ktn1 = u.ponto_para_virgula(busca_contas[3][7] / busca_contas[3][10] * float(busca_contas[3][6]))
            mes3ktn2 = u.ponto_para_virgula(busca_contas[3][8] / busca_contas[3][10] * float(busca_contas[3][6]))
            mes3ktn3 = u.ponto_para_virgula(busca_contas[3][9] / busca_contas[3][10] * float(busca_contas[3][6]))
            mes3total = u.ponto_para_virgula(mes3total)
        else:
            mes3total = mes3ktn1 = mes3ktn2 = mes3ktn3 = 0    
        
        mes3kwh = str(busca_contas[3][5]).replace('.',',')
        
        return render_template('energia.html',
                                    busca_contas = busca_contas,
                                    mes1ktn1 = mes1ktn1,
                                    mes1ktn2 = mes1ktn2,
                                    mes1ktn3 = mes1ktn3,
                                    mes2ktn1 = mes2ktn1,
                                    mes2ktn2 = mes2ktn2,
                                    mes2ktn3 = mes2ktn3,
                                    mes3ktn1 = mes3ktn1,
                                    mes3ktn2 = mes3ktn2,
                                    mes3ktn3 = mes3ktn3,
                                    mes1total = mes1total,
                                    mes2total = mes2total,
                                    mes3total = mes3total,
                                    mes1kwh = mes1kwh,
                                    mes2kwh = mes2kwh,
                                    mes3kwh = mes3kwh,
                                    data1 = u.data_brasil(busca_contas[1][1]),
                                    data2 = u.data_brasil(busca_contas[2][1]),
                                    data3 = u.data_brasil(busca_contas[3][1])
                                )
    else:
        return render_template('login.html') 

     
@app.route('/editarenergia', methods=['GET'])
def editarenergia():
    if u.MinhaUrl.logado():
        url = u.MinhaUrl(request.url)
        id_energia= url.id()
        
        if id_energia == '00': # se a id for 00 o sistema vai abrir a tela de adicionar novo
            energia = '00'
        else:
            energia = Energia.busca_energia(id_energia) # senao recebe o imovel escolhido do banco
            
        return render_template  (
                                    'form_energia.html',
                                    energia = energia
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