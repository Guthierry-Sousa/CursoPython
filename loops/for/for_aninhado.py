# Exemplo com matriz

matriz = []

# Preenchendo a matriz

for i in range(3):
    linha = []
    for j in range(3):
        element = int(input(f"Informe o elemento ({i}x{j}): "))
        linha.append(element)
    matriz.append(linha)

# Exibindo a matriz

for linha in matriz:
    print(linha)