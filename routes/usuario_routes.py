from flask import Flask, jsonify, request, Blueprint
from conexao import conecta_db

from bd.usuario import listar_usuarios_bd, inserir_usuario_bd, login_bd

usuario_bp = Blueprint("usuario", __name__, url_prefix = "/usuarios")


@usuario_bp.route("/", methods=["GET"])
def listar_usuarios():
    conexao = conecta_db()
    usuarios = listar_usuarios_bd(conexao)
    return jsonify(usuarios)

@usuario_bp.route("/", methods=["POST"])
def salvar_usuario():
    conexao = conecta_db()
    dados = request.get_json()
    
    login = dados['login']
    senha = dados['senha']
    admin = dados['admin']
    
    inserir_usuario_bd(conexao, login, senha, admin)
    return jsonify({"message":"Usuário salvo com sucesso!"})


@usuario_bp.route("/login", methods=["POST"])
def login_usuario():
    conexao = conecta_db()
    dados = request.get_json()
    
    login = dados['login']
    senha = dados['senha']
    valida_login = login_bd(conexao, login, senha)

    if valida_login is True:
        return jsonify({"message":"Usuário logado com sucesso!"})
    else:
        return jsonify({"message":"Usuário ou senha inválidos."})
