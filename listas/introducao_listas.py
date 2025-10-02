# Listas em Python
produtos = ["celular", "tv", "monitor", "processador", "placa de vídeo"]

vendas = [1000, 2000, 1500, 17500, 5000]

# Índices
print(produtos[0])
print(vendas[0])

# Exemplo
for i in range(len(produtos)):

    print(f"Produto: {produtos[i]} | Vendas: {vendas[i]} unidades\n")

# Listas são mutáveis, ou seja, podemos inserir, modificar e deletar valores.
vendas[2] = 3000
print(vendas)
