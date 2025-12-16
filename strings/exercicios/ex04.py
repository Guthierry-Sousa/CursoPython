s = input("Informe um frase: ").strip()

if s:
    s_lista = s.split()
    print(f"\nPrimeira palavra da frase: {s_lista[0]}")
    print(f"\nA frase possui {(s.lower()).count("a")} letras 'a'.")
else:
    print("Frase digitada de maneira incorreta.")