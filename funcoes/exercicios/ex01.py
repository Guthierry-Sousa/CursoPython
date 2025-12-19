# Crie uma função que receba um número, e faz um contador regressivo a partir dele

def contagem_regressiva(num):

    for i in range(num, 0, -1):

        print(i)

n = int(input("Informe um número: "))

contagem_regressiva(n)