# Argumentos e parâmetros de funções

def somar(x,y): #x e y são parâmetros
    return x+y

soma = somar(10,10) #10 e 10 são argumentos
print(f"Soma 1 : {soma}")
# Tambem é possível passar vários argumentos

def somar_update(*x): # Com isso é possível passar quantos números for necessário
    return sum(x)

soma = somar_update(10,10,10,10,10)
print(f"Soma 2 : {soma}")

# Resumo: Parâmetros são as variáveis definidas na assinatura de uma função (os "espaços reservados"), enquanto Argumentos são os valores reais ou expressões passadas para a função quando ela é chamada, preenchendo esses parâmetros, sendo que parâmetros são formais (na definição) e argumentos são atuais (na chamada).
