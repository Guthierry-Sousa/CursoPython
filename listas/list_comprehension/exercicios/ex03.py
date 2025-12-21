# 1. Tamanho do Pedido de Compras

# Caso o estoque esteja abaixo de 1000 unodades, devemos fazer um pedido de 500 unidades
# Caso o estoque esteja abaixo de 200 unidades, devemos fazer um pedido de 1000 unidades

estoque = [
    ('BSA2199', 396),
    ('PPF5239', 251),
    ('BSA1212', 989),
    ('PPF2154', 449),
    ('BEB3410', 241),
    ('PPF8999', 527),
    ('EMB9591', 601),
    ('BSA3321', 120),
    ('PPF7744', 845),
    ('BEB1102', 78),
    ('EMB4420', 930),
    ('BSA9087', 412),
    ('PPF6631', 590),
    ('BEB7788', 265),
    ('EMB1209', 1040),
    ('BSA5566', 334),
    ('PPF3412', 190),
    ('BEB9901', 57),
    ('EMB7770', 860),
    ('BSA6644', 710),
    ('PPF2288', 455),
    ('BEB5540', 302),
    ('EMB3301', 150),
    ('BSA1120', 980),
    ('PPF9090', 610),
    ('BEB6700', 89),
    ('EMB5151', 740),
    ('BSA7789', 510),
    ('PPF4400', 275),
    ('BEB8899', 132)
]

# Estrutura de saída: (código, quantidade_pedida)

estoque_pedidos = {k: 500 if v >= 200 else 1000 for k,v in estoque}

for code, quantidade in estoque_pedidos.items():

    print(f"Código: {code} | Quantidade Pedida: {quantidade}")