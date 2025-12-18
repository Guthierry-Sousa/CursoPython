vendas = [
    ("20/08/2020", "Notebook", "Cinza", "516gb", 350 ,4000),
    ("20/08/2020", "Notebook", "Cinza", "516gb", 100 ,4000),
    ("20/08/2020", "Memória ram","Black", "16gb", 127 ,500),
    ("20/08/2020", "Memória ram","Black", "16gb", 33 ,500),
    ("20/08/2020", "Memória ram","Black", "16gb", 100 ,500),
    ("21/08/2020", "Notebook", "Cinza", "516gb", 200 ,4000),
    ("21/08/2020", "Notebook", "Cinza", "516gb", 10 ,4000),
    ("21/08/2020", "Notebook", "Cinza", "516gb", 600 ,4000),
]

# Qual foi o faturamento total?

faturamento = 0

for data, produto, cor, capacidade, unidades, valor in vendas:

    faturamento += (unidades * valor)

print(f"O faturamento total foi de: R${faturamento:.2f}")

# Qual foi o faturamenrto de notebook no dia 20/08/2020?

faturamento_notebook = 0

for data, produto, cor, capacidade, unidades, valor in vendas:

    if((data.strip() == '20/08/2020') and (produto.lower().strip() == 'notebook')):
        faturamento_notebook += (unidades * valor)

print(f"O faturamento em 20/08/2020 de notebook foi de: R${faturamento_notebook:.2f}")

# Qual foi o produto mais vendido em unidades no dia 21/08/2020

produto_mais_vendido = ''
maior_quantidade_vendas = 0

for data, produto, cor, capacidade, unidades, valor in vendas:

    if unidades > maior_quantidade_vendas and data.strip() == '21/08/2020':

        maior_quantidade_vendas = unidades
        produto_mais_vendido = produto

print(f"O produto mais vendido em 21/08/2020 foi: '{produto_mais_vendido.upper()}' com {maior_quantidade_vendas} unidades vendidas.")

        
    

