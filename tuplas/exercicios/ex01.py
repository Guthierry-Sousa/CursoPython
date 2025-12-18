# 1. Análise de Vendas

meta = 10000

vendas = [
    ('João', 15000),
    ('Maria', 27000),
    ('Elis', 9900),
    ('Guthierry', 10500),
]

for nome, qtd_vendida in vendas:

    if qtd_vendida >= meta:

        print(f"Funicionário: {nome}. Bateu a meta com {qtd_vendida} vendas realizadas.")