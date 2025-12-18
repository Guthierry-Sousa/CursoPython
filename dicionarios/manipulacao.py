# Adicionar, Remover e Modificar itens no Dicionário

import random
# Adicionando Itens:

lucro_por_mes2025 = {}

for i in range(3):

    mes = input(f"Informe o mês {i+1}: ")
    lucro = random.randint(1000,10000)

    #Adicionando:
    lucro_por_mes2025[mes.capitalize()] = lucro

    print(f"\nMês: {mes.capitalize().strip()} | Lucro: R${lucro:.2f}\n")


# Modificando itens

print(lucro_por_mes2025)

lucro_por_mes2025['Janeiro'] = random.randint(1000,10000) # Modificação no mês de janeiro

print(f"Dicionário modificado (mês de janeiro): {lucro_por_mes2025}")


# Removendo Itens:

del lucro_por_mes2025['Janeiro'] # Deletando o mês de janeiro
print(lucro_por_mes2025)

# O pop tambem pode ser utilizado

mes = input("Informe o mês que vc quer remover: ")

valor_removido = lucro_por_mes2025.pop(mes)

print(f"Mes remoido = {mes} | Valor removido: {valor_removido}")

