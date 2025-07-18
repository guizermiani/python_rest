from conexao import conecta_db

def listar_categoria(conexao):
    cursor = conexao.cursor()
    # Execução do select no banco de dados
    cursor.execute("select id,nome from categoria order by id asc")
    # recuperar todos registros
    registros = cursor.fetchall()
    categorias = []
    for registro in registros:
        categoria = {
            "id": registro[0],
             "nome": registro[1]
         }
        categorias.append(categoria)
    return categorias







def consultar_categoria_por_id(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from categoria where id = " + str(id))
    registro = cursor.fetchone()

    if registro is None:
        return {"message": "Categoria não encontrada."}
    else:
        dados = {
            "id": registro[0],
             "nome": registro[1]
        }
        return dados

def inserir_categoria_bd(conexao, nome):
    print("Inserindo o Categoria ..: ")
    cursor = conexao.cursor()
    sql_insert = "insert into categoria (nome) values ('" + nome + "')"
    cursor.execute(sql_insert)
    conexao.commit()

def atualizar_categoria(conexao):
    print("Alterando dados dos Categoria")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    nome = input("Nome :")
    sql_update = "update categoria set nome ='" + nome + "' where id = "+ id
    cursor.execute(sql_update)
    conexao.commit()

def deletar_categoria(conexao):
    print("Deletando Categoria")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    sql_delete = "delete from categoria where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()
