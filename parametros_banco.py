import json

def parametros():
    arquivo = open('credenciais.txt', 'r')
    dicionario = json.loads(arquivo.read())
    arquivo.close()
    return dicionario






				
