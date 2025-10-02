# Print de listas: Método join -> texto.join(lista)

produtos = ["celular", "tv", "monitor", "processador", "placa de vídeo", "cadeira gamer", "placa-mãe"]

print(" | ".join(produtos))

produtos = "celular, tv, monitor, processador, placa de vídeo, cadeira gamer, placa-mãe"

lista = produtos.split(", ")
print(lista)