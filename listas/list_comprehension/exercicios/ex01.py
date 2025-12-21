# 1 - Tirando informações de listas e dicionários

#Estrutura = [(produto, venda2019, venda2020)]

vendas_produtos = [
    ('iphone', 558147, 951642),
    ('galaxy', 712350, 244295),
    ('ipad', 573823, 26964),
    ('tv', 405252, 787604),
    ('notebook', 682410, 154230),
    ('mouse', 98230, 845320),
    ('teclado', 145780, 392845),
    ('monitor', 358940, 128450),
    ('headset', 214670, 295630),
    ('impressora', 189540, 65430),
    ('roteador', 167890, 178230),
    ('ssd', 324560, 289430),
    ('hd_externo', 298340, 194520),
    ('pendrive', 76540, 584230),
    ('smartwatch', 245670, 184530),
    ('tablet', 312890, 97340),
    ('camera', 456780, 65420),
    ('drone', 587430, 34820),
    ('console', 634890, 98210),
    ('controle', 123450, 284530),
    ('cadeira_gamer', 278940, 74320),
    ('fonte', 189230, 129430),
    ('placa_mae', 345670, 98450),
    ('processador', 789430, 54230),
    ('placa_video', 1245670, 38940),
    ('memoria_ram', 298760, 213450),
    ('cooler', 98760, 342150),
    ('gabinete', 176540, 87540),
    ('webcam', 134560, 158930),
    ('microfone', 223450, 94320),
    ('celular_motorola', 1245670, 38940),
    ('celular_xiaomi', 1245670, 38940)
]

# Crie uma lista com as vendas de 2019

vendas_2019 = [venda[1] for venda in vendas_produtos]
print(vendas_2019)

# Qual o maior valor de vendas em 2019?

max_2019 = max(vendas_2019)
print(f"Maior valor de vendas em 2019: {max_2019}")

# Qual/Quais o(s) produto(s) que mais vendeu/venderam em 2019?

produto_max = [produto for produto, venda2019, _ in vendas_produtos if venda2019 == max_2019]


print("\n ------------- Produto(s) mais vendidos ------------- \n")
for i in range(len(produto_max)):

    print(f"Produto: {produto_max[i]} || Vendas: {max_2019} unidades")





