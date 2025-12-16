# O enumerate permite que você percorra uma lista e ao mesmo tempo tenha em uma variável o índice daquele item.

funcionarios = ["Elis Maria", "Elen Maria", "Guthierry Sousa", "Paulo Mesquita"]

for i, funcionario in enumerate(funcionarios):

    print(f"Nome: {funcionario} | Índice: {i}")

# Exemplo prático:
# - Identifique quais produtos estão abixo do nível mínimo de estoque.
# - Utilizando Enumerate
ESTOQUE_MINIMO = 50

estoque = [1200, 10, 300, 100, 90, 5, 6, 23]
produtos = ["Celular", "Mouse", "Notebook", "Teclado", "SSD", "Processador", "Memória Ram", "Fonte 500W"]

for i, qtd_estoque in enumerate(estoque):

    if qtd_estoque < ESTOQUE_MINIMO:

        print(f"\nProduto: {produtos[i]} | Estoque Atual: {qtd_estoque} | Compra mínima necessária: {ESTOQUE_MINIMO - qtd_estoque}")

print("\n------------------------------------------------------\n")

# - Utilizando ZIP (não precisa mais do índice)

for produto, qtd_estoque in zip(produtos,estoque):

    if qtd_estoque < ESTOQUE_MINIMO:

        print(f"\nProduto: {produto} | Estoque Atual: {qtd_estoque} | Compra mínima necessária: {ESTOQUE_MINIMO - qtd_estoque}")