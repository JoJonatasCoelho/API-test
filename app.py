from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

empregados = [
    {
        "id": "1",
        "nome": "Roberto",
        "cargo": "desenvolvedor",
        "salario": "5000"
    },
    {
        "id": "2",
        "nome": "Junior",
        "cargo": "desenvolvedor",
        "salario": "2000"
    },
    {
        "id": "3",
        "nome": "John",
        "cargo": "desenvolvedor",
        "salario": "10000"
    }
            ]


@app.route("/")
def home():
    return render_template("home.html")


# Create
@app.route('/empregados', methods=['POST'])
def createemploye():
    new_empregado = request.get_json()
    if not isinstance(new_empregado, dict):
        return jsonify({'Message': "Invalid data"}), 400
    required_keys = ['id', 'nome', 'cargo', 'salario']
    if not all(key in new_empregado for key in required_keys):
        return jsonify({'Message': "Missing required keys"}), 400
    for index, empregado in enumerate(empregados):
        if empregado.get('id') == new_empregado.get('id'):
            return jsonify({'Message': "Empregado's ID already exist"}), 400
    empregados.append(new_empregado)
    return jsonify(empregados), 201


# Read
@app.route("/empregados", methods=['GET'])
def todosempregados():
    return jsonify(empregados), 201


@app.route("/empregados/<info>/<valor>", methods=['GET'])
def procuraempregado(info, valor):
    out_empregados = []
    for empregado in empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]
            if type(value_empregado) == str:
                if valor == value_empregado:
                    out_empregados.append(empregado)
    return out_empregados, 201


# Update
@app.route('/empregados/<eid>', methods=['PUT'])
def modifyempregado(eid):
    new_empregado = request.get_json()
    if not isinstance(new_empregado, dict):
        return jsonify({'Message': "Invalid data"}), 400
    required_keys = ['id', 'nome', 'cargo', 'salario']
    if not all(key in new_empregado for key in required_keys):
        return jsonify({'Message': "Missing required keys"}), 400
    out_empregados = []
    for index, empregado in enumerate(empregados):
        if empregado.get('id') == eid:
            empregados[index].update(new_empregado)
            out_empregados.append(empregado)
            return jsonify(out_empregados)
    return jsonify({'message': 'Empregado dont founded'})


# Delete
@app.route('/empregados/<eid>', methods=['DELETE'])
def delempregado(eid):
    for index, empregado in enumerate(empregados):
        if empregado.get('id') == eid:
            empregados.pop(index)
            return jsonify(empregados)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
