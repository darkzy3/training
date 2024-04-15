from flask import Flask, request, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET'])
def add():
    # Récupérer les valeurs 'a' et 'b' de la requête
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a + b
    return jsonify({"result": result})

@app.route('/min', methods=['GET'])
def min():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a - b
    return jsonify({"result": result})

@app.route('/mul', methods=['GET'])
def mul():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a * b
    return jsonify({"result": result})

@app.route('/div', methods=['GET'])
def div():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    result = a / b
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
