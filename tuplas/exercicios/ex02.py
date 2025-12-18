#2. Comparação com o ano anterior

# (produto, vendas2019, vendas2020)

vendas_produtos = [('Notebook', 2000, 23455), ('Processador Intel', 2000, 5000), ('Teclado Mecâncico', 100, 45)]

for produto, venda2019, venda2020 in vendas_produtos:

    if venda2019 < venda2020:

        crescimento = (venda2020/venda2019) - 1

        print(f"Produto: {produto} | Vendas 2019: {venda2019} | Vendas 2020: {venda2020} | Procentagem de crescimento: {crescimento:.2%}")