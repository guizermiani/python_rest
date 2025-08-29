from flask import Flask, jsonify, request, Blueprint
from conexao import conecta_db
from bd.vendas import inserir_venda

venda_bp = Blueprint("venda", __name__, url_prefix = "/vendas")

@venda_bp.route("/", methods=["POST"])
def salvar_venda():
    conexao = conecta_db()
    dados = request.get_json()
    inserir_venda(conexao, dados)
    return jsonify({"message":"Venda salva com sucesso!"})