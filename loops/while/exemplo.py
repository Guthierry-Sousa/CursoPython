# 1. Input até o usuário parar

vendas = []

while True:

    dados_venda = []

    nome_produto = input("Informe seu nome: ").upper().strip()
    if nome_produto == "":
        break

    quantidade = int(input("Informe a quantidade de produtos vendidos: "))

    dados_venda.append(nome_produto)
    dados_venda.append(quantidade)

    vendas.append(dados_venda)

print("\nPrograma Finalizado!\n")

for i in vendas:
    print(f"Produto: {i[0]} | Quantidade de Vendas: {i[1]}")
    

