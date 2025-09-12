from flask import Flask, jsonify, request
from conexao import conecta_db
from bd.categoria import inserir_categoria_bd, consultar_categoria_por_id, listar_categoria, atualizar_categoria_bd, deletar_categoria_bd
from bd.produto import listar_produto_bd, consultar_produto_por_id_bd, inserir_produto_bd, atualizar_produto_bd, deletar_produto_bd

from routes.categoria_routes import categoria_bp
from routes.produto_routes import produto_bp
from routes.usuario_routes import usuario_bp
from routes.vendas_routes import venda_bp
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'designcursos'
    jwt = JWTManager(app)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(produto_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(venda_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug = True)