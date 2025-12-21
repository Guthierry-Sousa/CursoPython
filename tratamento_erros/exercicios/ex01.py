def leiaInt():

    while True:
        try:
            i = int(input("Informe um número inteiro: "))
            break
        except (ValueError, TypeError):
            print("Erro: Valor Inválido Digitado.")

        except KeyboardInterrupt:
            print("Erro: O usuário preferiu não informar este valor.")

            return 0

    return i


def leiaFloat():

    while True:
        try:
            i = float(input("Informe um número decimal: "))
            break

        except (ValueError, TypeError):
            print("Erro: Valor Inválido Digitado.")

        except KeyboardInterrupt:
            print("Erro: O usuário preferiu não informar este valor.")

            return 0

    return i


i = leiaInt()

f = leiaFloat()

print(f"\nO número inteiro digitado foi {i}\n")
print(f"\nO número decimal digitado foi {f}\n")
