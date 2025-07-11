from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"mensagem": "Hello World!" })

@app.route("/categorias/<int:id>", methods=["GET"])
def categoria_por_id(id):
    print("Informação ID")
    print(id)
    return jsonify({"id": id })

@app.route("/categorias", methods=["POST"])
def salvar_categoria():
    dados = request.get_json()
    return jsonify(dados)




if __name__ == "__main__":
    app.run()