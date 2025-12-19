# Funções podem retornar uma variável ou mais.

# Exemplo: Calcular média

def calcular_media(*n):

    return sum(n)/len(n)

media = calcular_media(10,2,4,5,6,7)

# Exemplo: Calculcar desvio padrao

def calcular_desvio_padrao(*n, mean):

    somatorio = 0

    for i in n:

        somatorio += ((i - mean)**2)

    dp = (somatorio/len(n))**0.5

    return dp

desvio_p = calcular_desvio_padrao(10,2,4,5,6,7, mean = media)

print(f"Média = {media:.2f} | DP = {desvio_p:.2f}\n")

# Retornando media e dp na mesma função

def estatistica(*n):

    m = sum(n)/len(n)

    somatorio = 0

    for i in n:

        somatorio += (i - m)**2

    dp = (somatorio/len(n))**0.5

    return m,dp

media_aritmetica, desvio_padrao = estatistica(10,2,4,5,6,7)

print(f"Média = {media_aritmetica:.2f} | DP = {desvio_p:.2f}\n")






