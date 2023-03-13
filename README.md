### Bem-Vindo ao meu curso na udemy, espero que goste, criei um projeto no github para ajudar com demais informações extra.

### Básico sobre utilizado:

**API:** interface de programação de aplicativos. Este é o conjunto de "comandos" que você usa para manipular o WebDriver.
**Biblioteca:** um módulo de código que contém as APIs e o código necessário para implementá-las. As bibliotecas são específicas para cada ligação de idioma, por exemplo, arquivos .jar para Java, arquivos .py para Python, etc.  
**Driver:** Responsável por controlar o navegador real. A maioria dos drivers é criada pelos próprios fornecedores do navegador. Drivers geralmente são módulos executáveis ​​executados no sistema com o próprio navegador, e não no sistema executando o conjunto de testes. (Embora esses possam ser o mesmo sistema.) NOTA: Algumas pessoas se referem aos drivers como proxies.  
**Estrutura:** uma biblioteca adicional usada como suporte para os conjuntos WebDriver. Essas estruturas podem ser estruturas de teste como JUnit ou BDD/Behave.
 
# udemy_my_course
Informação úteis sobre o curso, tem bastante coisa no meu github para compartilhar com a comunidade, o meu curso na udemy é de python 3 e Selenium com foco em resolver problemas.

**Seção 2: HTML Básico** >> Aprender a estrutura básica de uma página HTML é necessário pra qualquer pessoa que está ingressando em um curso sobre Automação Web.<br>
**Seção 3: Configurando o Ambiente** >> Aprendendo a configura e montar um ambiente de testes, como boa prática instalamos maquinas virtuais para trabalhar com automação.<br>
**Seção 4: PIP - Instalando os Pacotes** >> Precimos primeiramente entender como faz a instalação dos pacotes em python e como faz um requirements.txt em um projeto, aprender isso é a base de instalação e configuração das bibliotecas.<br>
**Seção 5: Pycharm e Atom Dicas** >> Algumas dicas sobre as IDEs.<br>
**Seção 6: Python Básico** >> O básico de python pra fazer uma automação, temos mais informação no github.<br>
**Seção 7: Selenium WebDriver Básico I** >> Agora sim vamos falar sobre o Selenium e suas classes, é somente uma introdução sobre as classes e um teste básico no Selenium WebDriver.<br>
**Seção 8: WebDriver - Intermediário** >> Agora vamos complicar um pouco falar sobre a DOM, Classe ActionChains, JavaScript.<br>
**Seção 9: Problemas e Truques com o Selenium** >> Agora sim vamos resolver e falar sobre alguns problemas.<br>
**Seção 10: Server & TestLink - Iniciando nosso Projeto** >> Precisamos instalar algumas ferramentas pra começar nosso projeto com o Behave.<br>
**Seção 11: Behave Básico** >> Vamos iniciar um projeto completo com behave, agora vamos falar da estrutura de um projeto de automação.<br>
**Seção 12: Behave - Environment Controls** >> Agora vamos aprender a parte de configuração do behave.<br>
**Seção 13: Passando Parâmetros e Scenario Outline** >> Agora vamos aprender a criar cenários mais elaborados.<br>
**Seção 14: Avançado - Problemas e Soluções** >> Resolvendo problemas do dia a dia.<br>
**Seção 15: Considerações Finais** >> Código fonte do nosso projeto.<br>
**Seção 16: News (Novidades)** >> Seção que vai falar sobre novidades no mundo de testes.<br>
**Seção 17: Desafios de Automação** >> É no final temos o nosso desafio, quem resolver, por favor me mande o github, e terá várias indicações minhas pra vagas.<br>

### Baixando o Projeto e Rodando os Testes nas Paginas HTML 
Passo a Passo:

1. Primeiro precisamos baixar o projeto no github, na sua maquina local.
```
git clone https://github.com/reinaldorossetti/udemy_behave_curso.git
```
2. Entrar na pasta do modulo que esta fazendo.
```
cd udemy_behave_curso
cd S07 - Selenium Basico
```
3. Vamos levantar um http server com o comando abaixo, insira o comando no console da IDE ou Terminal e der Enter:
```
python -m http.server --bind 127.0.0.1 8083
```
4. Subindo Agora sim somente rodar o teste que a página estará disponível.
```
http://localhost:8083/html/login.htm
```

Na pasta exemplo_selenium_mult_linguagem, vamos comparar as linguagens fazendo um teste simples em python e comparando com as outras linguagens, não vamos ficar ofendido a respeito disso por favor!

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
A vantagem dessa opção By, que ele mostra as opções quando digital By na IDE.
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

** A espera implicita só precisa ser aplicado uma vez, ela cria um delay no poll do driver internamente, uma vez aplicando ela agi sobre todos os find_element, não precisando fazer uma espera explicita depois, somente aplicando ela já funcionaria.


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

Na procura do elemento podemos trabalhar com a classe By, dessa forma o tipo do elemento "css selector" que passamos na função find, ficaria mais simples e genérica, como no exemplo abaixo:

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://github.com/")

# Nesse caso nao eh mais necessario a espera Implicita, somente temos um elemento e a explicita vai esperar.
# driver.implicitly_wait(3)

# dando um click no sign in no github.
sign_in = (By.CSS_SELECTOR, '.text-bold.text-white.no-underline')
user = (By.ID, 'login_field')
password = (By.ID, 'password')
submit = (By.NAME, 'commit')


def find(driver, *selector, delay=30):
    return WebDriverWait(driver, delay).until(expected_conditions.visibility_of_element_located(*selector))


find(driver, sign_in).click()
find(driver, user).send_keys("rei@gmail.com")
find(driver, password).send_keys("1234")
find(driver, password).send_keys(Keys.ENTER) # simulando um enter via keyboard.
```

** O uso da espera implicita junto com a Explícita, geralmente você usa uma ou outra, se usar as duas, vai gerar um delay a mais desnecessário, a não ser no caso de uma espera alta esperada de determinado elemento e queira usar como se fosse um segundo check, nesse caso aconselho a deixar a espera implicita com valor bem baixo de 3 a 5 segundos.

Vamos discutir tudo isso no curso e mais coisas, como a estrutura do nosso projeto, pensa que essa função find eu vou utilizar em N testes e eu não preciso repetir ela N vezes, devemos criar uma classe chamada BasePage que vai conter todas as funções genéricas do nosso projeto. <br>
Em muitos projetos que vejo por aí o pessoal utiliza mal o selenium, chamando as mesmas coisas várias vezes e torna o projeto um mostrinho e depois diz que o problema é o framework que não funciona, isso vai depender do seu domínio do framework e sobre a estrutura que vai usar no projeto.


Subindo o site localmente http://localhost:3000/users/new

1 - Abra o prompt de comando e abra na pasta de sia preferência e clone o projeto do github com o seguinte comando:
```
git clone https://github.com/brunobatista25/best_power.git
```

2 - Acesse a pasta do projeto via promt de comando com o comando (o caminho abaixo pode mudar):
```
cd caminho/da/pasta/com/o/nome/best_power
```

3 - dentro da pasta do projeto no prompt de comando execute o seguinte comando:
```
docker build -t imagem_site .
```

4 - E por último no prompt de comando execute o seguinte comando:
```
docker-compose up
```



5 - valide se o site estar no ar acessando o navegador através da url http://localhost:3000/

** Na Automação altera pra esse endereço.

**Primeiro passo instalando o Python:**
https://github.com/reinaldorossetti/udemy_my_course/blob/master/Instalando_o_python.MD

**Configurando o Ambiente:**
https://github.com/reinaldorossetti/udemy_my_course/blob/master/Configuracao_de_Ambiente.md

**Falando um pouco de Python:**
https://github.com/reinaldorossetti/udemy_my_course/blob/master/Um_pouco_de_python.md

**Falando a localização do elemento no Selenium WebDriver:**
https://github.com/reinaldorossetti/udemy_my_course/blob/master/selenium-python/docs/locating_elements.MD

**Falando sobre atributos e propriedades:**
https://github.com/reinaldorossetti/udemy_my_course/blob/master/pegando_valores.md
 
**Passo a Passo sobre instalação do TestLink:**
https://github.com/reinaldorossetti/udemy_my_course/blob/master/TestLink.MD
 
 **Básico sobre o Behave Framework:**  
https://github.com/reinaldorossetti/udemy_my_course/blob/master/Behave.MD
