# Estrutura de repetição while - normalmente é usada quando não se sabe a quantidade de repetições a serem feitas.

# Somatório de números até digitar 0

sum = 0

while True:

    num = int(input("Informe um número: "))
    if num == 0:
        break # Comando de parada
    sum += num
    print(f"Somatório atual: {sum}")

print(f"\nSomatório Total = {sum}")

