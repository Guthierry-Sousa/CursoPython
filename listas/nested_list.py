# Listas de Listas

vendedores = ["Elis", "Elen", "Yago", "Guthy"]
produtos = ["ipad", "iphone"]
vendas = [
    [100,200],
    [300,100],
    [200,130],
    [90,500],
]

for i in range(len(vendedores)):

    print(f"\n{vendedores[i]} vendeu {vendas[i][0]} unidades de {produtos[0]} e {vendas[i][1]} unidades de {produtos[1]}\n")

print("=====================================================")
# Alterando Valores

vendas[0][0] = 150

for i in range(len(vendedores)):

    print(f"\n{vendedores[i]} vendeu {vendas[i][0]} unidades de {produtos[0]} e {vendas[i][1]} unidades de {produtos[1]}\n")

# Adicionando Vendas de Novos produtos

vendas_mec = [10,15,6,70]

produtos.append("mac")

for i in range(len(vendas_mec)):

    vendas[i].append(vendas_mec[i])

print(vendas)


