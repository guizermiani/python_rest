from conexao import conecta_db
from flask import jsonify
import bcrypt

def login_bd(conexao, login, senha) -> str:
    cursor = conexao.cursor()
    cursor.execute("SELECT id, login, senha FROM usuario WHERE login = %s", (login,))
    registro = cursor.fetchone()

    if registro: # Verificando se o usuario foi encontrado
        senha_verificar = senha.encode("utf-8")

        senha_bd = registro[2]

        if isinstance(senha_bd, str):
            senha_bd_bytes = senha_bd.encode("utf-8")
        else:
            senha_bd_bytes = senha_bd
            
        if bcrypt.checkpw(senha_verificar, senha_bd_bytes):
             return "Usuário logado com sucesso!"
        else:
             return "Senha inválida."
        
    else:
        return "Usuário não encontrado."
       

def listar_usuarios_bd(conexao):
    cursor = conexao.cursor()
    sql_listar = """select id, login, admin from usuario          
                    order by id asc
                 """
    
    # Execução do select no banco de dados
    cursor.execute(sql_listar)
    # recuperar todos registros
    registros = cursor.fetchall()
    usuarios = []
    for registro in registros:
        usuario = {
            "id": registro[0],
             "nome": registro[1]  
        }
        usuarios.append(usuario)
    return usuarios
        
        
        


def consultar_usuario_por_id(conexao):
    id = input("Digite o ID: ")
    cursor = conexao.cursor()
    cursor.execute("select id,login,admin, from usuario where id = " + id)
    registro = cursor.fetchone()

    if registro is None:
        print("Usuário não encontrado:")
    else:
        print(f"| ID        ..: {registro[0]} ")
        print(f"| Login       : {registro[1]} ")
        print(f"| Admin       : {registro[2]} ")
       

def inserir_usuario_bd(conexao, login, senha, admin):
    print("Inserindo o Usuário ..: ")
    cursor = conexao.cursor()
    
    senha_bytes = senha.encode("utf-8")
    salt = bcrypt.gensalt() # Gera um salt aleatório
    hash_senha = bcrypt.hashpw(senha_bytes, salt)
    
    sql_insert = "insert into usuario (login,senha,admin) values ( %s, %s, %s )"
    dados = (login, hash_senha.decode('utf-8'), admin)
    cursor.execute(sql_insert, dados)
    conexao.commit()

def atualizar_usuario(conexao):
    print("Alterando dados do Usuário")
    cursor = conexao.cursor()

    id    = input("Digite o ID : ")
    login = input("Login: ")
    senha = input("Senha: ")
    admin = input("Admin: ")

    sql_update = "update usuario set login = %s, senha = %s, admin = %s where id = %s"
    dados = (login,senha,admin,id)

    cursor.execute(sql_update,dados)
    conexao.commit()

def deletar_usuario(conexao):
    print("Deletando Usuário")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    sql_delete = "delete from usuario where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()

def trocar_senha_bd(conexao, login, senha, novaSenha, confirmarSenha) -> str:
    cursor = conexao.cursor()
    cursor.execute("SELECT id, login, senha FROM usuario WHERE login = %s", (login,))
    registro = cursor.fetchone()

    if registro: # Verificando se o usuario foi encontrado
        senha_verificar = senha.encode("utf-8")

        senha_bd = registro[2]
        id_usuario = registro[0]

        if isinstance(senha_bd, str):
            senha_bd_bytes = senha_bd.encode("utf-8")
        else:
            senha_bd_bytes = senha_bd
            
        if bcrypt.checkpw(senha_verificar, senha_bd_bytes):
            if novaSenha == confirmarSenha:
                    senha_bytes = novaSenha.encode("utf-8")
                    salt = bcrypt.gensalt() # Gera um salt aleatório
                    hash_senha = bcrypt.hashpw(senha_bytes, salt)


                    sql_update = "update usuario set senha = %s  where id = %s"
                    dados = (hash_senha.decode('utf-8'), id_usuario)
                    cursor.execute(sql_update,dados)
                    conexao.commit()
                    return "Senha alterada com sucesso!"
            else:
              return "Nova senha e Confirmar senha não são iguais!"
            
        else:
             return "Senha atual inválida."
        
    else:
        return "Usuário não encontrado."