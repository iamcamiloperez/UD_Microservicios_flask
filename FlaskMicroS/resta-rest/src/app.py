from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/api/restar', methods=['GET'])
def ping():
    return jsonify({"response": "servicio restar"})

@app.route('/api/restar', methods=['POST'])
def restar_numeros():
    if not request.json or not 'numbers' in request.json :
        abort(400)

    result = 0

    for numbers, numbers_list in request.json.items():
        for pair in numbers_list:
            nextdict = pair
            for numberValue, number_list in nextdict.items():
                try:
                    if result != 0:
                        result = result - int(nextdict[numberValue])
                    else:
                        result = int(nextdict[numberValue])
                except:
                    abort(404)

    response = {  
        "result": result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=41010, debug=True)

