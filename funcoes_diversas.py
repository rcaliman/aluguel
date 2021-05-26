from flask import session, request
from classe_usuario import Usuario

def logado():
    if session:
        return True
    
