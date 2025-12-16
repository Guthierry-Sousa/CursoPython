# Introdução a estrutura for (ideal para listas)

produtos = ["coca", "pepsi", "quarana", "sprite", "fanta"]
producao = [15000, 12000, 13000, 5000, 250]

for produto, qtd_producao in zip(produtos, producao):

    print(f"\nProduto:{produto.capitalize()} | Produção: {qtd_producao} unidades.\n") 