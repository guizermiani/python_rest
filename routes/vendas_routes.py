from flask import Flask, jsonify, request, Blueprint
from conexao import conecta_db
from bd.vendas import inserir_venda, listar_vendas_bd

venda_bp = Blueprint("venda", __name__, url_prefix = "/vendas")

from flask_jwt_extended import jwt_required

@venda_bp.route("/", methods=["POST"])
@jwt_required()
def salvar_venda():
    conexao = conecta_db()
    dados = request.get_json()
    inserir_venda(conexao, dados)
    return jsonify({"message":"Venda salva com sucesso!"})

@venda_bp.route("/", methods=["GET"])
@jwt_required()
def listar_vendas():
    conexao = conecta_db()
    vendas = listar_vendas_bd(conexao)
    return jsonify(vendas)