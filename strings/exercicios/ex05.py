def is_palindromo(palavra):

    if palavra == palavra[::-1]:

        return True
    
    return False

word = input("Informe uma palavra: ")

if is_palindromo(word):
    
    print(f"\nA palavra {word} é um palíndromo")

else:

    print(f"\nA palavra {word} não é um palíndromo")