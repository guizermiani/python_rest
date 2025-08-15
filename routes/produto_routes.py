from flask import Flask, jsonify, request, Blueprint
from bd.produto import listar_produto_bd, consultar_produto_por_id_bd, inserir_produto_bd, atualizar_produto_bd, deletar_produto_bd
from conexao import conecta_db


produto_bp = Blueprint("produto", __name__, url_prefix = "/produtos")


@produto_bp.route("/", methods=["GET"])
def listar_produtos():
    conexao = conecta_db()
    produtos = listar_produto_bd(conexao)
    return jsonify(produtos)

@produto_bp.route("/<int:id>", methods=["GET"])
def consultar_produto_por_id(id):
    conexao = conecta_db()
    produtos = consultar_produto_por_id_bd(conexao,id)
    return jsonify(produtos)

@produto_bp.route("/", methods=["POST"])
def salvar_produto():
    dados = request.get_json()
    nome = dados["nome"]
    valor_venda = dados["valorVenda"]
    estoque = dados["estoque"]
    categoria_id = dados["categoriaId"]
    
    conexao = conecta_db()
    inserir_produto_bd(conexao, nome, valor_venda, estoque, categoria_id)
    return jsonify({"message": "Produto salvo com sucesso." })



@produto_bp.route("/<int:id>", methods = ["PUT"])
def alterar_produto(id):
    dados = request.get_json()
    nome = dados["nome"]
    valor_venda = dados["valorVenda"]
    estoque = dados["estoque"]
    categoria_id = dados["categoriaId"]
    
    conexao = conecta_db()
    atualizar_produto_bd(conexao, nome, valor_venda, estoque, categoria_id, id)
    return jsonify({"message": "Produto alterado com sucesso." })

@produto_bp.route("/<int:id>", methods=["DELETE"])
def excluir_produto_por_id(id):
    conexao = conecta_db()
    deletar_produto_bd(conexao, id)
    return jsonify({"message": "Produto excluído com sucesso." })