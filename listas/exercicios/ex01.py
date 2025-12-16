#Crie uma lista com os quadrados dos números ímpares de 1 a 20. (List comprehension)

square = [x**2 for x in range(1,21)]

print("Quadrados dos números de 1 até 20 na sequência:")
print(square)