from conexao import conecta_db
from datetime import datetime
  
def consultar_vendas():
    print("Não Implementado")

def insert_item_venda(conexao, item_venda):
    cursor = conexao.cursor()
    sql_insert_item = """
        insert into itens_venda(id_venda,id_produto,qtde,valor_unitario, valor_total)
        values(%s, %s, %s, %s, %s)
    """
    cursor.execute(sql_insert_item, item_venda)
    conexao.commit()


def inserir_venda(conexao, dados):
    id_cliente = dados['idCliente']
    numero_venda = dados['numeroVenda']

    itens = dados['itensVenda']
    venda = alimentar_venda(id_cliente, numero_venda)

    itens_venda = alimentar_itens_venda(itens)
    total_venda = calcular_total_venda(itens_venda)

    id_venda = insert_venda(conexao, venda, total_venda)

    for item in itens_venda:
         item_data = (id_venda, item['id_produto'], item['quantidade'],
         item['preco_unitario'], item['valor_total'])
    insert_item_venda(conexao, item_data)

def alimentar_venda(id_cliente, numero_venda):
    data_venda = datetime.now()
    valor_venda = 0
    return (id_cliente, data_venda, numero_venda, valor_venda)

def insert_venda(conexao, venda, total_venda):
    cursor = conexao.cursor()
    sql_insert_venda = """
        insert into venda(id_cliente, data_venda, numero_venda, valor_venda)
        values (%s, %s, %s, %s) RETURNING id;
    """
    dados_venda = (venda[0],venda[1],venda[2], total_venda)
    cursor.execute(sql_insert_venda, dados_venda)
    venda_id = cursor.fetchone()[0]
    conexao.commit()
    return venda_id

def alimentar_itens_venda(itens):
    itens_venda = []
    for item in itens:
        id_produto = item['idProduto']
        quantidade= item['quantidade']
        preco_unitario = item['precoUnitario']
        valor_total = float(quantidade) * float(preco_unitario)

        itens_venda.append({"id_produto": id_produto,
                            "quantidade": quantidade,
                            "preco_unitario": preco_unitario,
                            "valor_total": valor_total})
        print(itens_venda)

    return itens_venda
        
def calcular_total_venda(itens_venda):
            total_venda = 0
            for item in itens_venda:
                total_venda = total_venda + item['valor_total']
            return total_venda

def listar_vendas_bd(conexao):
    cursor = conexao.cursor()
    sql_listar = """select v.id, v.numero_venda, c.nome, v.valor_venda 
                    from venda v
                    inner join cliente c on v.id_cliente = c.id
                    order by v.numero_venda asc, v.valor_venda desc
                 """
    
    cursor.execute(sql_listar)

    registros = cursor.fetchall()

    vendas = []
    for registro in registros:
        venda = {
            "numero_venda": registro[1],
            "nome_cliente": registro[2],
            "valor_venda": registro[3],
        }
        vendas.append(venda)
    return vendas