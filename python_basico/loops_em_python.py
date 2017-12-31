# primeira forma de fazer, criando um determinado range de inicio e fim.
for x in range(0, 3): # Inicia em zero e para em 3.
    print("Quantidade de Loops:{}".format(x)) # vai imprimir o a mensagem três vezes.

# segunda forma de fazer iterando dentro de um string.
palavra = "curso de selenium"
for x in palavra:
    print(x) # vai imprimir letra por letra da nossa palavra.

# podemos usar um matriz/array para iterar em uma lista de numeros ou palavras.
cores = ["amarelo", "azul", "preto", "vermelho"]
for cor in cores:
    print(cor)

numeros = [33,24,56,78,99]
for numero in numeros:
    print(numero)

# Melhorando nosso código pode usar a palavra reservada **enumerate**,
# para mostrar a localização da cor na lista.
cores = ["amarelo", "azul", "preto", "vermelho"]
for index, cor in enumerate(cores):
    print("index:{} cor:{}".format(index,cor))

# podemos usar para listar um dicionario em python.
dicionario = {1:"amarelo",2:"azul", 3:"preto", 4:"vermelho"}
for key, valor in enumerate(cores):
    print("chave:{} valor:{}".format(key, valor))