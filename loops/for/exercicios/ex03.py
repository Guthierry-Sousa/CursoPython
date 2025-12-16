# 1. Calculando % de uma lista

meta = 1000

vendas = [
    ["João", 15000],
    ["Júlia", 100],
    ["Elis", 800],
    ["Marcus", 900],
    ["Ana", 100],
]

# Verificar a porcentagem de vendedores que bateram a meta

vendedores_com_meta_batida = []

for i in vendas:

    if i[1] >= meta:

        vendedores_com_meta_batida.append(i)

porcentagem = (len(vendedores_com_meta_batida) * 100)/len(vendas)

print(f"Porcentagem de vendedores que bateram a meta de vendas: {porcentagem}%")

# Verificar o vendedor que mais vendeu
funcionario_com_mais_vendas = max(vendas, key = lambda vendas: vendas[1])

print(f"Funcionário que mais vendeu foi {funcionario_com_mais_vendas[0]} com {funcionario_com_mais_vendas[1]} unidades vendidas.")

    