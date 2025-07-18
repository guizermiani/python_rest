from flask import Flask, jsonify, request
from categoria import inserir_categoria_bd, consultar_categoria_por_id, listar_categoria
from conexao import conecta_db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({"mensagem": "Hello World!" })

@app.route("/categorias", methods=["GET"])
def todas_categorias():
    conexao = conecta_db()
    categoria = listar_categoria(conexao)
    return jsonify(categoria)

@app.route("/categorias/<int:id>", methods=["GET"])
def categoria_por_id():
    conexao = conecta_db()
    categoria = consultar_categoria_por_id(conexao, id)
    return jsonify(categoria)

@app.route("/categorias", methods=["POST"])
def salvar_categoria():
    dados = request.get_json()
    nome = dados["nome"]
    conexao = conecta_db()
    inserir_categoria_bd(conexao, nome)
    return jsonify({"message": "Categoria salva com sucesso." })

@app.route("/categorias/<int:id>", methods=["PUT"])
def atualizar_categoria(id):
    print("ID passado por parâmetro")
    print(id)
    dados = request.get_json()
    nome = dados["nome"]
    status = dados["status"]
    print(nome)
    print(status)
    return jsonify(dados)


@app.route("/categorias/<int:id>", methods=["DELETE"])
def excluir_categoria_por_id(id):
    return jsonify({"message": "Categoria excluída com sucesso." })



if __name__ == "__main__":
    app.run()