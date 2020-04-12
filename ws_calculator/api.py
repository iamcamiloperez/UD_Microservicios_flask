import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Actividad informática - Operaciones</h1>
<p>Se plantea establecer una arquitectura orientada a microservicios usando el micro-framework flask para ofrecer la implementación de los servicios de suma, resta, multiplicación y división.</p>'''


#Operación suma
#http://localhost:5000/ws_calculator/v1/resources/operation/sum?n[0]=4&n[1]=2
@app.route('/ws_calculator/v1/resources/operation/sum', methods=['GET'])
def api_sum():
    if request.args:
        # We have our query string nicely serialized as a Python dictionary
        args = request.args
        resultado = 0

        # We'll create a string to display the parameters & values
        for k, v in request.args.items():
            try:
                resultado += float(v)
            except:
                resultado += 0
        return str(resultado), 200
    else:
        return "No se recibieron parametros", 400 

#Operación resta
#http://localhost:5000/ws_calculator/v1/resources/operation/res?n[0]=4&n[1]=2
@app.route('/ws_calculator/v1/resources/operation/res', methods=['GET'])
def api_res():
    if request.args:
        # We have our query string nicely serialized as a Python dictionary
        args = request.args
        resultado = 0

        # We'll create a string to display the parameters & values
        for k, v in request.args.items():
            try:
                resultado -= float(v)
            except:
                resultado -= 0
        return str(resultado), 200
    else:
        return "No se recibieron parametros", 400 

#Operación multiplicacion
#http://localhost:5000/ws_calculator/v1/resources/operation/mul?n[0]=4&n[1]=2
@app.route('/ws_calculator/v1/resources/operation/mul', methods=['GET'])
def api_mul():
    if request.args:
        # We have our query string nicely serialized as a Python dictionary
        args = request.args
        resultado = 0
        index = 0
        # We'll create a string to display the parameters & values
        for k, v in request.args.items():
            try:
                if index == 0:
                    resultado = float(v)
                else:
                    resultado *= float(v)
                index+=1
            except:
                resultado = 0
        return str(resultado), 200
    else:
        return "No se recibieron parametros", 400 

#Operación división
#http://localhost:5000/ws_calculator/v1/resources/operation/div?n[0]=4&n[1]=2
@app.route('/ws_calculator/v1/resources/operation/div', methods=['GET'])
def api_div():
    if request.args:
        # We have our query string nicely serialized as a Python dictionary
        args = request.args
        resultado = 0
        index = 0
        # We'll create a string to display the parameters & values
        for k, v in request.args.items():
            try:
                if index == 0:
                    resultado = float(v)
                else:
                    resultado /= float(v)
                index+=1
            except:
                resultado = 0
        return str(resultado), 200
    else:
        return "No se recibieron parametros", 400 


app.run()