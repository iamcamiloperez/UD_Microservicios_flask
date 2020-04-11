import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Actividad informática - Operaciones</h1>
<p>Se plantea establecer una arquitectura orientada a microservicios usando el micro-framework flask para ofrecer la implementación de los servicios de suma, resta, multiplicación y división.</p>'''


#Operación suma
#http://localhost:5000/ws_calculator/v1/resources/operation/sum
@app.route('/ws_calculator/v1/resources/operation/sum', methods=['GET'])
def api_sum():
    return 'operacion sumar'

#Operación resta
#http://localhost:5000/ws_calculator/v1/resources/operation/res
@app.route('/ws_calculator/v1/resources/operation/res', methods=['GET'])
def api_res():
    return 'operacion restar'

#Operación multiplicacion
#http://localhost:5000/ws_calculator/v1/resources/operation/mul
@app.route('/ws_calculator/v1/resources/operation/mul', methods=['GET'])
def api_mul():
    return 'operacion multiplicar'

#Operación división
#http://localhost:5000/ws_calculator/v1/resources/operation/div
@app.route('/ws_calculator/v1/resources/operation/div', methods=['GET'])
def api_div():
    return 'operacion dividir'


app.run()