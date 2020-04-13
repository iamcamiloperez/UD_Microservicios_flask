from flask import Flask, jsonify, request, abort
from usesrs import users

app = Flask(__name__)

@app.route('/api/sumar', methods=['GET'])
def ping():
    return jsonify({"response": "servicio sumar"})

@app.route('/api/users')
def userHandler():
    return jsonify({"users": users})

@app.route('/api/sumar', methods=['POST'])
def sumar_numeros():
    if not request.json or not 'numbers' in request.json :
        abort(400)

    result = 0

    for numbers, numbers_list in request.json.items():
        for pair in numbers_list:
            nextdict = pair
            for numberValue, number_list in nextdict.items():
                #print('print each: ' + str(numberValue)+ '->' + str(number_list))
                #address each one                
                result = result + int(nextdict[numberValue])

    response = {  
        "result": result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=41000, debug=True)

