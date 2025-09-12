from flask import Flask, jsonify, request, Blueprint
from bd.categoria import inserir_categoria_bd, consultar_categoria_por_id, listar_categoria, atualizar_categoria_bd, deletar_categoria_bd
from conexao import conecta_db
from flask_jwt_extended import jwt_required


categoria_bp = Blueprint("categoria", __name__, url_prefix = "/categorias")


    
@categoria_bp.route("/", methods=["GET"])
@jwt_required()
def todas_categorias():
    conexao = conecta_db()
    categoria = listar_categoria(conexao)
    return jsonify(categoria)

@categoria_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def categoria_por_id(id):
    conexao = conecta_db()
    categoria = consultar_categoria_por_id(conexao, id)
    return jsonify(categoria)

@categoria_bp.route("/", methods=["POST"])
@jwt_required()
def salvar_categoria():
    dados = request.get_json()
    nome = dados["nome"]
    conexao = conecta_db()
    inserir_categoria_bd(conexao, nome)
    return jsonify({"message": "Categoria salva com sucesso." })

@categoria_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar_categoria(id):
    print("ID passado por parâmetro")
    print(id)
    dados = request.get_json()
    nome = dados["nome"]
    print(nome)
    conexao = conecta_db()
    atualizar_categoria_bd(conexao,id,nome)
    return jsonify({"message": "Categoria atualizada com sucesso."})

@categoria_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir_categoria_por_id(id):
    conexao = conecta_db()
    deletar_categoria_bd(conexao, id)
    return jsonify({"message": "Categoria excluída com sucesso." })
