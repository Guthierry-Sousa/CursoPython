# Cálculo do Percentual e da Lista de Vendedores

def calular_percentual_meta(meta, dicionario_funcionaros):

    funcionarios_bateram_meta = []

    for nome, vendas in dicionario_funcionaros.items():

        if vendas >= meta:

            funcionarios_bateram_meta.append(nome)

    percentual_bateram_meta = len(funcionarios_bateram_meta)/len(dicionario_funcionaros)

    return funcionarios_bateram_meta, percentual_bateram_meta


#Dados
meta_vendas = 10000
vendas = {
    'Elis': 15000,
    'Elen': 27000,
    'Guthierry': 9900,
    'Nicolas': 3750,
    'Ana': 7870
}

funcionarios, percentual = calular_percentual_meta(meta_vendas, vendas)

print(f"Funcionários que bateram a meta: {" | ".join(funcionarios)}")
print(f"A porcentagem de funcionarios foi de {percentual:.2%}")


