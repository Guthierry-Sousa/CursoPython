# Dicionário: {key, value}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300}

qtd_vendas_iphone = vendas_tecnologia['iphone'] # Passa por index a key e retorna o value

print(f"Quandidade de iphones vendidos: {qtd_vendas_iphone}")

#Utilizando .get() - caso a chave não exista, retorna None:

# Exemplo: 

item = input("Informe o item que vc quer ver a quantidade de vendas: ")

if vendas_tecnologia.get(item):

    print(f"Item: {item} | Vendas: {vendas_tecnologia[item]}")

else:

    print("Não possuimos este produto em tecnologia.")
