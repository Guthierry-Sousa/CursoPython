# Crie uma função que recebe uma lista e retorne o maior numero desta lista

# Forma simples
def maior_numero(lista_numeros):

    return max(lista_numeros)

# Forma mais complexa
def max_numero(lista_numeros):

    maior_n = lista_numeros[0]

    for num in lista_numeros:

        if(num > maior_n):

            maior_n = num

    return maior_n


n = int(input("Informe a quantidade de iterações: "))

lista = []

for i in range(n):

    num = int(input("Informe um número: "))

    lista.append(num)

max_value = maior_numero(lista)
print(f"O maior número entre '{lista}' é {max_value}. (Utilizando a função simples)")

max_value = max_numero(lista)
print(f"O maior número entre '{lista}' é {max_value}. (Utilizando a função complexa)")




