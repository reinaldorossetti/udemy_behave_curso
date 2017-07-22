# udemy_my_course
Exemplo usados no meu curso na udemy de python 3 e Selenium.

Na pasta exemplo_selenium_mult_linguagem, vamos comparar as linguagens fazendo um teste simples.

### Vamos primeiro analisar a quantidade de caracteres sem os espaços:
https://github.com/reinaldorossetti/udemy_my_course/blob/master/SELENIUM_MULT_LINGUAGEM_EXEMPLOS.md


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
Existe uma forma de instanciar o driver utilizando o selenium-server que é um arquivo.jar, nele podemos passar o nome do browser.
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

Os nomes das funções nomeiadas com termos compostos exemplo `getTitle()` usam a formatação camelCase do Java, mas no python elas ficam minúsculas. Por exemplo em python temos a função `title` e em Java temos a função `getTitle ()`, em muitas funções a palavra fica separada por subtraço (_), traço rasteiro ou underscore:

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
driver.find_element('css selector', '//h1').click()
```


