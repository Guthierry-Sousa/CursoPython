# Tupla é uma estrutura imutável, ou seja , não é possível modificar (inserir, alterar e excluir) elementos.

#Exemplo

dados_func1 = ("Guthierry", "04/01/2007", 2000, "Estariário")

nome1, data_nascimento1, salario1 , cargo1 = dados_func1

print(dados_func1)

print(f"\nNome: {nome1} | Nascimento: {data_nascimento1} | Salário: {salario1} | Cargo: {cargo1}\n")

# A função enumerate que usamos em listas, na verdade, cria uma tupla (índice, valor).

