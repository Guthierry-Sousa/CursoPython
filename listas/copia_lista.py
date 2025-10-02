# Copiar e Igualdade de Listas

lista = [x for x in range(0,10,2)]

print(lista)

# Primeira forma
lista_2 = lista[:] 
print(lista)

# Segunda forma
lista_3 = lista.copy()
print(lista_3)

# Caso eu modifique algumas das cópias não modifica a original