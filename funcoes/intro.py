# Funções são blocos de código que fazem uma ação específica

#Exemplo: função/procedimento hello

def hello(name):
    print(f"Hello {name}, how are you?")

n = input("Informe seu nome: ")

hello(n)

#Exemplo: cadastrar e exibir produtos

def cadastrar_produto(lista_produtos):
    n = int(input("Informe a quantidade de produtos para cadastrar: "))
    for i in range(n):
        p = input("Informe o nome do produto: ").lower().strip()
        lista_produtos.append(p)
    return lista_produtos
    
def exibir_produtos(lista_produtos):
    for produto in lista_produtos:
        print(f"\nProduto '{produto}' foi cadastrado no sistema.")

produtos = []
cadastrar_produto(produtos)
exibir_produtos(produtos)




