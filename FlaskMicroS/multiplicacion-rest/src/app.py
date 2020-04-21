from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/api/multiplicar', methods=['GET'])
def ping():
    return jsonify({"response": "servicio multiplicar"})

@app.route('/api/multiplicar', methods=['POST'])
def multiplicar_numeros():
    if not request.json or not 'numbers' in request.json :
        abort(400)

    result = 1

    for numbers, numbers_list in request.json.items():
        for pair in numbers_list:
            nextdict = pair
            for numberValue, number_list in nextdict.items():
                try:
                    result = result * int(nextdict[numberValue])
                except:
                    abort(404)

    response = {  
        "result": result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=41020, debug=True)

