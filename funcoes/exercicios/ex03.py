# Cálculo de carga tributária

def calcular_carga_tributaria(preco, custo, lucro):
    imposto = preco - (custo + lucro)

    carga_tributaria = imposto/preco

    return carga_tributaria

p = 1000
c = 500
l = 100

ct = calcular_carga_tributaria(p, c, l)

print(f"A carga tributária sobre o produto de preço total {p} foi de : {ct:.1%}")