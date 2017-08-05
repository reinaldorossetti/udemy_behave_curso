

Nesse tutorial vamos falar o básico de Python.

Começando a falar de python o que notamos de cara ao olhar para o código fonte, é que ele não tem colchetes "{" "}" para iniciar um bloco de código, ele é orientado a indentação, ou seja atrávez dos espaçamentos ele sabe aonde inicia e fechar um bloco de código.

1. O padrão de espaçamento entre a funçao deve ser igual a 4 espaços dentro da função, função é nada menos que um bloco de código com uma funcionalidade específica, exemplo:
```python

x = 0 # inicio do meu codigo, criei uma variavel que recebe o valor 0.
def nome_da_funcao(string):
    deve_ter_4_espacos_aqui += 1
    valor = deve_ter_4_espacos_aqui
    print(string+str(valor)) # a função str convert o valor numerico para string/texto.
    
# finalizou_a_funcao_e_voltei_pro_inicio
nome_da_funcao("Valor: ") # fiz a chamada da minha função, nessa linha.
```
O **print** no meu código é a função que vai imprimir o valor no console ou shell/cmd/prompt.


2. No python como devemos importar um biblioteca, é regra básica importar as bibliotecas no inicio do seu código. A importação deve ser separada por linhas, não é aconselhado a importar tudo em uma linha só

Imports should usually be on separate lines, e.g.:

Fazer assim
```python
import os
import sys
```

Não fazer:  
```python
import sys, os
```

Segunda foram de fazer a importação: 
```python:
from subprocess import Popen, PIPE
```
Pior forma de fazer, está importando tudo pra memória, mesmo você não usando:  
```python
from subprocess import *
```
