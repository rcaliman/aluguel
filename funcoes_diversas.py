from flask import session, request
from classe_usuario import Usuario
from urllib.parse import urlparse
from urllib import parse

def logado():
    if session:
        return True
    
def extrai_id_da_url(url):
    dic = parse.parse_qs(urlparse(url).query)
    return dic['id'][0]
    
