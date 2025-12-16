import random

meta = 1000

vendas = [random.randint(1,2000) for x in range(50)]
print(vendas)

cont_bateu_meta = 0

for i in vendas:

    if(i >= meta):

        cont_bateu_meta += 1

porcentagem_bateu_meta = (cont_bateu_meta*100)/len(vendas)

print(f"Porcentagem de vendas que bateram a meta: {porcentagem_bateu_meta}%")
    
