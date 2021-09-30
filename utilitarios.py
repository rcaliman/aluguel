from urllib.parse import urlparse
from flask import session
import datetime
from classe_energia import Energia
from classe_cliente import Cliente
from classe_imovel import Imovel
import numero_por_extenso
class MinhaUrl:
    def __init__(self, url):
        self.url = url
    
    def path(self):
        return urlparse(self.url).path
    
    def id(self):
        parte_id = str.split(urlparse(self.url).query,'&')[0]
        return str.split(parte_id,'=')[1]
        
    def acao(self):
        parte_acao = str.split(urlparse(self.url).query,'&')[1]
        return str.split(parte_acao,'=')[1]
    
    @staticmethod
    def logado():
        if session:
            return True

def input_ano():
    data = datetime.datetime.now()
    ano = data.year
    input = f""" <select name='ano' class="form-select">
                    <option value="{ano-1}">{ano-1}</option>
                    <option selected value="{ano}">{ano}</option>
                    <option value="{ano+1}">{ano+1}</option>
                </select>"""
    return input

def input_mes():
    data = datetime.datetime.now()
    mes = data.month
    input = """<select name='mes' class="form-select">
                        <option value="janeiro">janeiro</option>
                        <option value="fevereiro">fevereiro</option>
                        <option value="marco">marco</option>
                        <option value="abril">abril</option>
                        <option value="maio">maio</option>
                        <option value="junho">junho</option> 
                        <option value="julho">julho</option>
                        <option value="agosto">agosto</option>
                        <option value="setembro">setembro</option> 
                        <option value="outubro">outubro</option>
                        <option value="novembro">novembro</option>
                        <option value="dezembro">dezembro</option></select>"""
    if mes == 1:
        novo_input = input.replace('value="janeiro">','value="janeiro" selected>')
    elif mes == 2:
        novo_input = input.replace('value="fevereiro">','value="fevereiro" selected>')
    elif mes == 3:
        novo_input = input.replace('value="marco">','value="marco" selected>')
    elif mes == 4:
        novo_input = input.replace('value="abril">','value="abril" selected>')
    elif mes == 5:
        novo_input = input.replace('value="maio">','value="maio" selected>')
    elif mes == 6:
        novo_input = input.replace('value="junho">','value="junho" selected>')
    elif mes == 7:
        novo_input = input.replace('value="julho">','value="julho" selected>')
    elif mes == 8:
        novo_input = input.replace('value="agosto">','value="agosto" selected>')
    elif mes == 9:
        novo_input = input.replace('value="setembro">','value="setembro" selected>')
    elif mes == 10:
        novo_input = input.replace('value="outubro">','value="outubro" selected>')
    elif mes == 11:
        novo_input = input.replace('value="novembro">','value="novembro" selected>')
    else:
        novo_input = input.replace('value="dezembro">','value="dezembro" selected>')

    return novo_input


def busca_contas():
    tudo = Energia.busca_contas(4)
    lista = []
    # cria uma nova lista a partir da tupla
    for i in tudo:
        lista.append(list(i))    

    cont = 0   
    x = 0 
    for linha in lista:
        if cont > 0:
            lista[cont].append(linha[2] - ktn1)
            lista[cont].append(linha[3] - ktn2)
            lista[cont].append(linha[4] - ktn3)
            lista[cont].append(linha[2] + linha[3] + linha[4] - ktn1 - ktn2 - ktn3)
        for dado in linha:
            ktn1 = linha[2] 
            ktn2 = linha[3]
            ktn3 = linha[4]
        cont += 1
    return lista

                
def ponto_para_virgula(variavel):
    variavel = str('{:0.2f}'.format(variavel)).replace('.',',')
    return variavel

def data_brasil(data):
    data = str.split(str(data),'-')
    nova_data = f"{data[2]}/{data[1]}/{data[0]}"
    return nova_data

def virgula_para_ponto(valor):
    valor = str(valor).replace(',','.')
    return valor

def recibos(dados_recibo, mes, ano):
    try:
        telefones = f'<em style="padding-left:30px;font-size: 0.8em">{str(Cliente.seleciona_telefones(dados_recibo[4])[0][0])}</em>'
        telefones += f'<em style="padding-left:30px;font-size: 0.8em">{str(Cliente.seleciona_telefones(dados_recibo[4])[0][1])}</em>'
    except:
        telefones = f'<em style="padding-left:30px;font-size: 0.8em">&nbsp;</em>'
    imovel = 'do' if dados_recibo[1][-1] in 'o' else 'da'
    html = f'<div style="font-family: \'Droid Sans Mono\';font-size: 1.5em;">'
    html += f'<center><h2 style="padding-top:0.5em" class="pointer" onclick=javascript:location.href="/imoveis"><u><b>RECIBO</b></u></h2></center>'
    html += f'<p>Recebi de <b><u>{dados_recibo[4]}</u></b> a importancia de {numero_por_extenso.monetario(dados_recibo[5])} '
    html += f'referente ao aluguel {imovel} {dados_recibo[1]} numero {dados_recibo[2]}.</p>'
    html += f'<p align=right style="padding-top: 1.2em">Colatina, {dados_recibo[7]} de {mes} de {ano}</p>'
    html += f'<center style="padding-top: 1.2em">___________________________________________________</center>'
    html += f'<center>Darci Francisco Caliman<br>proprietário</center>'
    html += f'<p align=right style="padding-bottom: 1.2em">{telefones}</p>'
    html += f'</div>'
    html += f'<hr style="border-top: 1px dashed; margin-bottom: 1.2em">'
    return html