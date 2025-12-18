# Utilizando dicionários com a estrutura de repetição for

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300}

for item in vendas_tecnologia.items():

    print(f"Produto: {item[0]} | Vendas: {item[1]} unidades")