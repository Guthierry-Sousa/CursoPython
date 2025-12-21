
def lerDinheiro(txt):
    while True:
        dinheiro = input(txt).strip().replace(",", ".")
        try:
            return float(dinheiro)
        except ValueError:
            print("\nValor inválido.\n")


