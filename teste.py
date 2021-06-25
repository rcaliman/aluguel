from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'inicia'

@app.route('/segundo')
def segundo():
    teste = request.url
    return teste

@app.route('/terceiro')
def terceiro():
    return '<a href="http://localhost:5000/segundo">teste</a>'

app.run(debug=True)
