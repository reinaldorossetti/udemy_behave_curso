# udemy_my_course
Exemplo usados no meu curso na udemy de python 3 e Selenium.

Na pasta exemplo_selenium_mult_linguagem, vamos comparar as linguagens fazendo um teste simples.

### Vamos primeiro analisar a quantidade de caracteres sem os espaços:
https://github.com/reinaldorossetti/udemy_my_course/blob/master/SELENIUM_MULT_LINGUAGEM_EXEMPLOS.md


Seção 2: HTML Básico >> Aprender a estrutura básica de uma página HTML é necessário pra qualquer pessoa que está ingressando em um curso sobre Automação Web.
Seção 3: Configurando o Ambiente >> Aprendendo a configura e montar um ambiente de testes, como boa prática instalamos maquinas virtuais para trabalhar com automação.
Seção 4: PIP - Instalando os Pacotes >> Precimos primeiramente entender como faz a instalação dos pacotes em python e como faz um requirements.txt em um projeto, aprender isso é a base de instalação e configuração das bibliotecas.
Seção 5: Pycharm e Atom Dicas >> Algumas dicas sobre as IDEs.
Seção 6: Python Básico >> O básico de python pra fazer uma automação, temos mais informação no github.
Seção 7: Selenium WebDriver Básico I >> Agora sim vamos falar sobre o Selenium e suas classes, é somente uma introdução sobre as classes e um teste básico no Selenium WebDriver.
Seção 8: WebDriver - Intermediário >> Agora vamos complicar um pouco falar sobre a DOM, Classe ActionChains, JavaScript.
Seção 9: Problemas e Truques com o Selenium >> Agora sim vamos resolver e falar sobre alguns problemas.
Seção 10: Server & TestLink - Iniciando nosso Projeto >> Precisamos instalar algumas ferramentas pra começar nosso projeto com o Behave.
Seção 11: Behave Básico >> Vamos iniciar um projeto completo com behave, agora vamos falar da estrutura de um projeto de automação.
Seção 12: Behave - Environment Controls >> Agora vamos aprender a parte de configuração do behave.
Seção 13: Passando Parâmetros e Scenario Outline >> Agora vamos aprender a criar cenários mais elaborados.
Seção 14: Avançado - Problemas e Soluções >> Resolvendo problemas do dia a dia.
Seção 15: Considerações Finais >> Código fonte do nosso projeto.
Seção 16: News (Novidades) >> Seção que vai falar sobre novidades no mundo de testes.
Seção 17: Desafios de Automação >> É no final temos o nosso desafio, quem resolver, por favor me mande o github, e terá várias indicações minhas pra vagas.

# Realizando a instalação do Selenium Webdriver

O Projeto do Official do Selenium suporta as versões do python 2.7 e 3.6.

The latest official release is available on the [Python Package Index](http://python.org/pypi/selenium). It's a good practice to install python packages into [virtual environments](https://packaging.python.org/installing/#creating-and-using-virtual-environments) rather than in your global site packages. 

Para instalar a biblioteca/framework do Selenium utilizamos o comando oficial de instalação dos pacotes pip.
([pip](https://pip.pypa.io/en/stable/installing/)).

 Para realizar a instalação rodamos o comando abaixo no (shell, cmd, prompt do sistema operacional):

```
pip install selenium
```

# Passo a Passo de como usar os comandos:

Para utilizamos as funções do nosso framework, primeiro devemos Importar o módulo, digitando o seguinte comando abaixo no seu shell python/IDE:

```python
from selenium import webdriver
```

Depois de importa a biblioteca devemos instanciar o driver do Selenium, o driver vai fazer a conexão com browser, então o comando é diferente para cada browser, segue os exemplos abaixo de acordo com o browser:

### Firefox

```python
from selenium import webdriver
driver = webdriver.Firefox()
```

### Google Chrome

```python
from selenium import webdriver
driver = webdriver.Chrome()
```

### Internet Explorer

```python
from selenium import webdriver
driver = webdriver.Ie()
```

### Microsoft Edge

```python
from selenium import webdriver
driver = webdriver.Edge()
```

### Safari

```python
from selenium import webdriver
driver = webdriver.Safari()
```


### Remote Driver
Existe uma forma de instanciar o driver utilizando o selenium-server que é um arquivo.jar, nele podemos passar o nome do browser. Já tive a necessidade de utilizar o selenium-server.jar pra passar pelo proxy no IE utilizando o remote, o modo direto não conseguiu autenticar pelo proxy.
```python
from selenium import webdriver
driver = webdriver.Remote(browser_name="firefox", platform="any")
```


# Documentação do Selenium WebDriver

A documentação está disponível online [aqui] (http://seleniumhq.github.io/selenium/docs/api/py/) e pode ser construída localmente usando o comando `tox -e docs`.
## Interactive

Uma alternativamente via shell/prompt usando o console do python para visualizar todos os comandos disponíveis para você, após a importação, executamos o comando abaixo:
```python
dir(webdriver)
```

Para ver as docstrings  (texto da documentação anexado a uma função ou método), execute o comando abaixo:
```python
print(nome_da_funcao_fica_aqui.__doc__)
```
### Exemplo abaixo da função get do Firefox
```python
from selenium import webdriver
print(webdriver.Firefox.get.__doc__)
```
Mostra o Resultado:  Loads a web page in the current browser session.

## Abaixo alguns comparações basicas dos comandos em python e java

### Function Names

Os nomes das funções nomeadas com termos compostos exemplo `getTitle()` usam a formatação camelCase do Java, mas no python elas ficam minúsculas. Por exemplo em python temos a função `title` e em Java temos a função `getTitle ()`, em muitas funções a palavra fica separada por subtraço (_), traço rasteiro ou underscore:

Em python:
`find_element_by_xpath("//h1")`
Equivalente em Java:
`findElement(By.xpath("//h1"));`

Em python também podemos fazer de várias formas, primeiro pra usar o By devemos importando a classe By.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://github.com/")
# dando um click na logo do github.
driver.find_element(by=By.CSS_SELECTOR, value='.octicon.octicon-mark-github').click()
```
Ou
```python
driver.find_element(By.CSS_SELECTOR, '.octicon.octicon-mark-github').click()
```

Um truque que faço é assim de forma reduzida sem precisar da classe By.
```python
driver.find_element('css selector', '.octicon.octicon-mark-github').click()
```

Agora vamos separar o locator e o valor dele, deixando o código mais limpo
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://github.com/")

# organizando no inicio o tipo de locator e o valor dele, para não poluir o código.
css, sign_in = 'css selector', '.text-bold.text-white.no-underline'

# dando um click no sign in no github.
driver.find_element(css, sign_in).click()

```

Nosso código está muito ruim, pensa numa página HTML os elementos estão sendo carregados, o nosso código não tem nenhuma espera dos elementos, ou seja assim que carregar a url ele vai mandar os comandos fora de hora, o que vai fazer ele quebrar. Então para que ele não quebre, colocamos uma espera chamada de Implícita realizada pela função implicitly_wait. 

A espera Implicita de acordo com a documentação diz que vai esperar no máximo o valor que você colocou como máximo ou seja no nosso caso até 30 segundos. Não que dizer que vai esperar 30 segundos, pode terminar antes disso, vai depender da velocidade da sua internet. Existe outro tipo de espera que vamos falar mais à frente.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://github.com/")
driver.implicitly_wait(30) # Espera implicita para carregar os elementos na pagina HTML.

# organizando no inicio o tipo de locator e o valor dele, para não poluir o código.
css, sign_in = 'css selector', '.text-bold.text-white.no-underline'

# dando um click no sign in no github.
driver.find_element(css, sign_in).click()

```

Agora vamos falar de outro tipo de espera, a espera explícita, resumindo a espera explícita devemos especificar qual elemento devemos  esperar, na espera implícita ele espera todos os elementos, ele não espera um elemento específico, o que torna a espera explícita melhor por ser mais rápida. Geralmente eu coloco a espera implícita 15 segundos pra carregar a url e todos os elementos no inicio depois de dar o get pra carregar a url, mas somente uso uma vez. 
<b>
1. O primeiro passo que devemos fazer é importar as bibliotecas que vão realizar a espera explícita.

```python
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
```

2. O segundo passo é aplicar as funções, criamos uma função chamada find e nela fizemos a espera explícita de passando o driver, o nosso elemento web, e o delay máximo que desejamos. Na função aplicamos o tipo de espera explíta pela função visibility_of_element_located, quer dizer que esperar o elemento ser vísivel para o usuário, o retorno da nossa função vai ser o próprio elemento já mapeado, assim podemos aplicar as funções de click, send_keys entre outras.

```python
def find(driver, selector, delay=30):
    # Espera Explicita > Melhor forma de fazer.
    # An expectation for checking that an element is present on the DOM of a page and visible.
    return WebDriverWait(driver, delay).until(
        expected_conditions.visibility_of_element_located(("css selector", selector)))
```

O nosso código completo ficaria assim, eu não preciso mais fazer o driver.find_element, agora temos a função que vai realizar esse processo já com a espera explícita.

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://github.com/")
driver.implicitly_wait(15) # nesse caso nao eh mais necessario, somente temos um elemento e a explicita vai esperar.

# dando um click no sign in no github.
sign_in = '.text-bold.text-white.no-underline'

def find(driver, selector, delay=30):
    return WebDriverWait(driver, delay).until(
        expected_conditions.visibility_of_element_located(("css selector", selector)))

find(driver, sign_in).click()
```

Vamos discutir tudo isso no curso e mais coisas, como a estrutura do nosso projeto, pensa que essa função find eu vou utilizar em N testes e eu não preciso repetir ela N vezes, devemos criar uma classe chamada BasePage que vai conter todas as funções genéricas do nosso projeto. <br>
Em muitos projetos que vejo por aí o pessoal utiliza mal o selenium, chamando as mesmas coisas várias vezes e torna o projeto um mostrinho e depois diz que o problema é o framework que não funciona, isso vai depender do seu domínio do framework e sobre a estrutura que vai usar no projeto.

**Configurando o Ambiente:
https://github.com/reinaldorossetti/udemy_my_course/blob/master/Configuracao_de_Ambiente.md
