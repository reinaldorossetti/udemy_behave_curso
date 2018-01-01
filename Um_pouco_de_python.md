

Nesse tutorial vamos falar o básico de Python.

Começando a falar de python o que notamos de cara ao olhar para o código fonte, é que ele não tem colchetes "{" "}" para iniciar um bloco de código, ele é orientado a indentação, ou seja através dos espaçamentos ele sabe aonde inicia e fechar um bloco de código.

1. O padrão de espaçamento entre a funçao deve ser igual a 4 espaços dentro da função, função é nada menos que um bloco de código com uma funcionalidade específica, exemplo:
```python
"""
Pra fazer um comentário grande usamos três aspas duplas pra iniciar e pra fechar três aspas duplas.
Um comentário simples em uma linha usamos o jogo da velho/cerquilha #
"""

x = 0 # inicio do meu codigo, criei uma variavel que recebe o valor 0.
def nome_da_funcao(string):
    deve_ter_4_espacos_aqui += 1
    valor = deve_ter_4_espacos_aqui
    print(string+str(valor)) # a função str convert o valor numerico para string/texto.
    
# finalizou_a_funcao_e_voltei_pro_inicio
nome_da_funcao("Valor: ") # fiz a chamada da minha função, nessa linha.
```
O **print** no meu código é a função que vai imprimir o valor no console ou shell/cmd/prompt.
O **def** é uma definição que aqui vai estar uma função que pode ser retornada ou passada (def vem de function definition).
<br><br>

2. No python como devemos importar um biblioteca, é regra básica importar as bibliotecas no inicio do seu código. A importação deve ser separada por linhas, não é aconselhado a importar tudo em uma linha só

Fazer assim
```python
import os
import sys
```

Não fazer:  
```python
import sys, os
```

Segunda forma de fazer a importação, usando o **from**: 
```python:
from subprocess import Popen, PIPE
```
Pior forma de fazer, está importando tudo pra memória, mesmo você não usando:  
```python
from subprocess import *
```
<br><br>
3. Como trabalhar com condições em python, ou seja if e else.

```python

x = 5  # Criei uma variável x que vai receber um valor numerico 5.

# minha primeira condição, verifica se o valor é menor que 4.
if x < 1:
    print("valor incorreto!")
elif x == 4:  # minha segunda condição, verifica se o valor é igual a 1.
    print("valor incorreto!")
elif x >= 5 and x < 10:  # minha terceira condição, verifica se o valor é maior e igual a 5 e menor que 10.
    print("O valor esperado está correto!")
else: # O else é digamos se nenhuma das condições foi realizada, ele vai entrar nesse bloco de código.
    print("Nenhuma condição foi encontrada!")
```   
![alt text](http://diwo.bq.com/wp-content/uploads/2015/10/ifelse.png "Condição IF ELSE")

Tome muito cuidado quando for criar condições somente use quando for preciso, o excesso de condições pode deixar o código lento.

**Abaixo segue uma lista com os operadores aritméticos utilizados em Python:**

```python
+   # soma
–   # subtração
*   # multiplicação
/   # divisão
//  # divisão de inteiros
**  # potenciação, dois asteristicos.
%   # módulo (resto da divisão)
```

**Segue também os operadores lógicos:**
```python
>   # maior
=   # maior ou igual
<=  # menor ou igual
==  # igual
!=  # diferente
not # Operador lógico que representa a negação (inverso) da variável atual. Se ela for verdade, torna-se falsa, e vice-versa.
and # Operador lógico onde a resposta da operação é verdade se ambas as variáveis de entrada forem verdade.
or  # Operador lógico onde a resposta da operação é verdade se e somente se pelo menos uma das variáveis de entrada for verdade.
```

## Loops em Pyhton
Para Repetições/Loops, são usados tradicionalmente quando você tem um bloco de código que você deseja repetir, ou seja você repeti um número fixo de vezes. O Python para declaração "for" itera sobre os membros de uma seqüência em ordem, executando o bloco a cada vez. 

```python
# primeira forma de fazer, criando um determinado range de inicio e fim.
for x in range(0, 3): # Inicia em zero e para em 3.
    print("Quantidade de Loops:{}".format(x)) # vai imprimir o a mensagem três vezes.

# segunda forma de fazer iterando dentro de um string.
palavra = "curso de selenium"
for x in palavra:
    print(x) # vai imprimir letra por letra da nossa palavra.

# podemos usar um matriz/array para iterar um lista de numero ou palavras.
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
 ```

