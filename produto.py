from conexao import conecta_db

def listar_produto_bd(conexao):
    cursor = conexao.cursor()
    sql_listar = """select p.id,p.nome,p.valor_venda,p.estoque,
                        p.categoria_id as categoria_id,
                        c.id as id_categoria,
                        c.nome as nome_categoria
                  from produto p
               inner join categoria c on (p.categoria_id = c.id)
               order by p.id asc
         """
    
    # Execução do select no banco de dados
    cursor.execute(sql_listar)
    # recuperar todos registros
    registros = cursor.fetchall()
    
    produtos = []
    for registro in registros:
        produto = {
            "id": registro[0],
            "nome": registro[1],
            "valorVenda": registro[2],
            "estoque": registro[3],
            "nomeProduto": registro[6]
        }
        produtos.append(produto)
    return produtos
        
def consultar_produto_por_id_bd(conexao,id):
    cursor = conexao.cursor()
    cursor.execute("select id,nome,valor_venda, estoque from produto where id = " + str(id))
    registro = cursor.fetchone()

    if registro is None:
        return {"message": "Produto não encontrado."}
    else:
        dados = {
            "id": registro[0],
             "nome": registro[1],
             "valorVenda":registro[2],
             "estoque": registro[3]
     }
        return dados


def inserir_produto_bd(conexao):
    print("Inserindo o Produto ..: ")
    cursor = conexao.cursor()
    nome = input("Nome :")
    valor_venda = float(("Valor Venda :"))
    estoque = float(("Estoque :"))
    categoria_id = int(input("ID Categoria: "))

    sql_insert = "insert into produto (nome,valor_venda,estoque,categoria_id) values ( %s, %s,%s, %s )"
    dados = (nome,valor_venda,estoque,categoria_id)

    cursor.execute(sql_insert, dados)
    conexao.commit()

def atualizar_produto_bd(conexao):
    print("Alterando dados dos Produtos")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")

    nome = input("Nome :")
    valor_venda = float(("Valor Venda :"))
    estoque = float(("Valor Venda :"))

    sql_update = "update produto set nome = %s, valor_venda = %s, estoque = %s where id = %s"
    dados = (nome,valor_venda,estoque,id)

    cursor.execute(sql_update,dados)
    conexao.commit()

def deletar_produto_bd(conexao):
    print("Deletando Produto")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    sql_delete = "delete from produto where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()
