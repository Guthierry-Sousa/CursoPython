def aumentar(preco, taxa, format = True):

    taxa_porcentagem = taxa/100

    if format == False:
        return preco * (1+taxa_porcentagem)

    return formatar(preco * (1+taxa_porcentagem))


def diminuir(preco, taxa, format = True):

    taxa_porcentagem = taxa/100

    if format == False:
        return preco * (1-taxa_porcentagem)

    return formatar(preco * (1-taxa_porcentagem))


def dobrar(preco, format = True):

    if format == False:
        return preco*2

    return formatar(preco*2)


def metade(preco, format = True):

    if format == False:
        return preco/2

    return formatar(preco/2)

def formatar(preco):

    return f"R${preco:.2f}"

def resumo(preco, taxa_aumento, taxa_diminuicao, format = True):

    print("----------------------------")
    print("\n   RESUMO DO VALOR   \n")
    print("----------------------------\n")
    print(f"Preço analisado: {formatar(preco)}")

    print(f"A metade de {formatar(preco)} é {metade(preco, format)}")
    print(f"O dobro de {formatar(preco)} é {dobrar(preco, format)}")
    print(f"Aumentando {formatar(preco)} em {taxa_aumento}% = {aumentar(preco, taxa_aumento, format)}")
    print(f"Diminuindo {formatar(preco)} em {taxa_diminuicao}% = {diminuir(preco, taxa_diminuicao, format)}")
    print("\n----------------------------\n")
