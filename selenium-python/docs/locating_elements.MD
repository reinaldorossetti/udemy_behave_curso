### 1. Métodos para localizar elementos:

Existem várias estratégias para localizar elementos em uma página, um deles é usando o **BY**, ou usar os métodos de forma direta somente preenchendo o conteúdo do atributo. Você pode usar o mais apropriado para o seu caso. 
O Selenium fornece os seguintes métodos para localizar elementos em uma página, listamos todos abaixo:  

**  
find_element_by_id  
find_element_by_name  
find_element_by_xpath  
find_element_by_link_text  
find_element_by_partial_link_text  
find_element_by_tag_name  
find_element_by_class_name  
find_element_by_css_selector  
**

Para encontrar vários elementos (esses métodos retornarão uma lista/array):  
**
find_elements_by_name  
find_elements_by_xpath  
find_elements_by_link_text  
find_elements_by_partial_link_text  
find_elements_by_tag_name  
find_elements_by_class_name  
find_elements_by_css_selector  
**

Além dos métodos públicos fornecidos acima, existem dois métodos privados que podem ser úteis com localizadores em objetos de página.
Estes são os dois métodos particulares (private): **find_element e find_elements**.

Example de uso:
```
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com.br")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(15)

# interage somente com um elemento
driver.find_element(By.CSS_SELECTOR, 'input[title="Pesquisar"]').send_keys("Selenium")
driver.find_element(By.XPATH, '//input[@value="Pesquisa Google"]').click()

# exemplo de interação com varios elementos.
elementos01 = driver.find_elements(By.CSS_SELECTOR, 'input')
elementos02 = driver.find_elements(By.XPATH, '//button')

# conta a quantidade de elementos de input e button.
print( "{} - {}".format(len(elementos01), len(elementos02)))

driver.quit()
```

Abaixo temos os atributos da classe By:
```
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

Ao invés de localizar os elementos via By, podemos fazer isso diretamente, exemplo:

```
# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com.br")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(15)

# interage somente com um elemento
driver.find_element_by_css_selector('input[title="Pesquisar"]').send_keys("Selenium")
driver.find_element_by_xpath('//input[@value="Pesquisa Google"]').click()

# exemplo de interacao com varios elementos.
elementos01 = driver.find_elements_by_css_selector('input')
elementos02 = driver.find_elements_by_xpath('//button')

# conta a quantidade de elementos de input e button.
print( "{} - {}".format(len(elementos01), len(elementos02)))

driver.quit()
```

### 2. Localizando elementos por Id (é sempre a melhor opção de localização)

Deve usar quando tiver o atributo `id` no elemento esperado. Com essa
estratégia, o primeiro elemento com o atributo `id` correspondente
é retornado. Se nenhum dos elementos da pagina não tiver nenhum atributo **id** correspondente,
vai retornar um erro **NoSuchElementException** o erro será gerado nos logs de execução.

#### Example de uso:
~~~~~~~~~~~~~~
# https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_login_form
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/code/tryit.asp?filename=G0R1H2HWBRSG")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(15)

# interage somente com um elemento
driver.find_element_by_xpath('//button[contains(text(),"Run")]').click() # Nao tem ID, usamos o texto
driver.switch_to.frame("iframeResult")  # mudando para o frame que desejamos
# localizando o elemento por ID, nesse caso somente insiro o valor.
driver.find_element_by_id('uname').send_keys('Reinaldo')

# exemplo de interacao com varios elementos.
elementos01 = driver.find_elements_by_id('psw')
elementos01[0].send_keys('12345')
driver.find_elements_by_id('login')[0].send_keys(Keys.ENTER)

# verifica se nosso teste esta correto.
assert driver.title, "W3Schools Online Web Tutorials"

driver.quit()
~~~~~~~~~~~~~~~~

### 3. Localizando elemento por Name

Deve usar quando tiver o atributo name no elemento esperado. Com essa estratégia, o primeiro elemento com um atributo **name** correspondente será retornado. Se nenhum elemento tiver um atributo name correspondente, será gerado um **NoSuchElementException**. Segue o exemplo abaixo:


#### Example de uso:
~~~~~~~~~~~~~~~~
# https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_login_form
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/code/tryit.asp?filename=G0R1H2HWBRSG")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(15)

# interage somente com um elemento.
driver.find_element_by_xpath('//button[contains(text(),"Run")]').click() # Nao tem ID, usamos o texto
driver.switch_to.frame("iframeResult")  # mudando para o frame que desejamos
# localizando o elemento pelo atributo name
driver.find_element_by_name('uname').send_keys('Reinaldo')

# exemplo de interacao com varios elementos.
elementos01 = driver.find_elements_by_name('psw')
elementos01[0].send_keys('12345')
driver.find_elements_by_name('login')[0].send_keys(Keys.ENTER)

# verifica se nosso teste esta correto.
assert driver.title, "W3Schools Online Web Tutorials"

driver.quit()
~~~~~~~~~~~~~~~~~

### 4. Localizando elemento por CSS Selectors

Use quando o elemento não tiver **ID**, usando a sintaxe do seletor CSS. Com essa estratégia, o primeiro elemento correspondente ao seletor CSS especificado será retornado. Se nenhum elemento corresponder ao seletor CSS fornecido, um **NoSuchElementException** será gerado.

#### Example de uso:
~~~~~~~~~~~~~~~~
# https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_login_form
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/code/tryit.asp?filename=G0R1H2HWBRSG")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(15)

# interage somente com um elemento.
driver.find_element_by_css_selector('button[onclick*="try_it_leaderboard"]').click()
driver.switch_to.frame("iframeResult")  # mudando para o frame que desejamos
# localizando o elemento pelo atributo id, o # representa o id no css.
driver.find_element_by_css_selector('#uname').send_keys('Reinaldo')

# exemplo de interacao com varios elementos.
elementos01 = driver.find_elements_by_css_selector('#psw')
elementos01[0].send_keys('12345')
# forma reduzida, o [0] significa o primeiro elemento do meu array.
driver.find_elements_by_css_selector('#login')[0].send_keys(Keys.ENTER)

# verifica se nosso teste esta correto.
assert driver.title, "W3Schools Online Web Tutorials"

driver.quit()

~~~~~~~~~~~~~~~~

[Sauce Labs tem uma boa documentação do mesmo:](https://saucelabs.com/resources/articles/selenium-tips-css-selectors)


### 5. Localizando elemento por by XPath

XPath é a linguagem usada para localizar nós em um documento XML. Como o HTML pode ser uma implementação de XML (XHTML), os usuários do Selenium podem aproveitar essa linguagem poderosa para direcionar elementos em seus aplicativos da web. O XPath suporta os métodos simples de localização por atributos de identificação ou nome e os estende, abrindo todos os tipos de novas possibilidades, como localizar a terceira caixa de seleção na página.

Um dos principais motivos para usar o XPath é quando você não possui um atributo de id ou nome adequado para o elemento que deseja localizar. Você pode usar o XPath para localizar o elemento em termos absolutos (não recomendado) ou em relação a um elemento que possui um atributo de identificação ou nome. Os localizadores via XPath, também podem ser usados para especificar elementos por meio de atributos diferentes de id e nome.

XPaths absolutos contêm a localização de todos os elementos da raiz (html) e, como resultado, provavelmente falharão com apenas o menor ajuste no aplicativo. Ao localizar um elemento próximo com um atributo de ID ou nome (idealmente, um elemento pai), você pode localizar seu elemento de destino com base no relacionamento. É muito menos provável que isso mude e pode tornar seus testes mais robustos.

#### Example de uso:
```python
# https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_login_form
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/code/tryit.asp?filename=GBIE8VKXQWNG")
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(15)

# interage somente com um elemento
# geralmente se usa muito xpath para localizar o texto, esse foi o caso abaixo por não ter id.
# nesse caso vou usar o exato texto, no próximo vou usar o relativo.
driver.find_element_by_xpath('//button[text()="Run »"]').click()
driver.switch_to.frame("iframeResult")  # mudando para o frame que desejamos
# nesse caso vou usar o contains, que procura o elemento que contain a palavra Motion dentro do texto.
sistema_name = driver.find_element_by_xpath('//b[contains(text(),"Motion")]').text
assert "Motion" in sistema_name

# localizando o elemento por XPATH
driver.find_element_by_xpath('//input[@id="uname"]').send_keys('Reinaldo')

# exemplo de intercao com varios elemento
elementos01 = driver.find_elements_by_xpath('//input[@id="psw"]')
elementos01[0].send_keys('12345')
# forma reduzida, o [0] significa o primeiro elemento do meu array.
driver.find_elements_by_xpath('//button[@id="login"]')[0].send_keys(Keys.ENTER)

# verifica se nosso teste esta correto.
assert driver.title, "W3Schools Online Web Tutorials"

driver.quit()
```

#### Exemplo teórico page source:  
```HTML
   <html>
    <body>
     <form id="loginForm">
      <div class='a classe eh dinamica'>Sistema: Motion</div>
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
     </form>
   </body>
   <html>
```

O elementos HTML acima podem ser localizados da forma abaixo. 
~~~~~~~~~~~~~~~~~
  login_form = driver.find_element_by_xpath("/html/body/form[1]")          # 1  
  login_form = driver.find_element_by_xpath("//form[1]")                   # 2  
  login_form = driver.find_element_by_xpath("//form[@id='loginForm']")     # 3  
~~~~~~~~~~~~~~~~~

1. Caminho absoluto (seria interrompido se o HTML fosse alterado apenas um pouco).  

2. Primeiro elemento do formulário no HTML.  

3. O elemento do formulário com o atributo `id` definido como` loginForm` (Melhor forma de aplicar).  

O elemento **username** do usuário pode ser localizado assim:  
~~~~~~~~~~~~~~~~~
  username = driver.find_element_by_xpath("//form[input/@name='username']")  
  username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")  
  username = driver.find_element_by_xpath("//input[@name='username']")  
~~~~~~~~~~~~~~~~~


1. Criei um exemplo para localizar o nome do meu formulário, que nesse caso chamo de Motion.
** Uma coisa que tem que ter em mente, o *text* no xpath, ele não é um atributo (@) e sim um método, por isso o mesmo usa text() ao invés de @text.
~~~~~~~~~~~~~~~~~
  sistema_name = driver.find_element_by_xpath("//b[contains(text(),"Motion")]").text
~~~~~~~~~~~~~~~~~

2. Primeiro elemento do formulário com um elemento filho de entrada com 'name' definido como 'username'

3. Primeiro elemento filho de entrada do elemento de formulário com o atributo 'id' definido como 'loginForm'

4. Primeiro elemento de entrada com o atributo `name` definido como` username`

O elemento do botão "Limpar" pode ser localizado da forma abaixo:
~~~~~~~~~~~~~~~~~
  clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
  clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
~~~~~~~~~~~~~~~~~

1. Uma forma legal é definir vários atributos, `name` definido como` continue` e o atributo `type` definido como` button`.

2. Quarto elemento filho de entrada do elemento do formulário com o atributo `id` definido como `loginForm`.

Esses exemplos abrangem alguns princípios básicos, mas para saber mais, as seguintes referências são recomendadas:

* [W3Schools XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)
* [W3C XPath Recommendation](http://www.w3.org/TR/xpath)
* [XPath Tutorial](http://www.zvon.org/comp/r/tut-XPath_1.html)

### 6. Localizando Hyperlinks pelo Texto do Link
 
Geralmente esse opção é usada quando nenhuma das acimas é possível, você pode localizar pelo nome do link, no exemplo abaixo é feito pelo **Continue e Cancel**. Com essa estratégia, o primeiro elemento com o texto do link correspondente ao valor fornecido será retornado. Se nenhum elemento tiver um atributo de texto de link correspondente, será gerado um NoSuchElementException.

#### Exemplo teórico page source:  

```HTML
  <html>
   <body>
    <p>Are you sure you want to do this?</p>
    <a href="continue.html">Continue</a>
    <a href="cancel.html">Cancel</a>
  </body>
  <html>
```

O link continue.html pode ser localizado dessa forma::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  continue_link = driver.find_element_by_link_text('Continue')
  continue_link = driver.find_element_by_partial_link_text('Conti')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### 7. Localizando o elemento pela Tag Name

Use quando desejar localizar um elemento pelo nome da tag. Com essa estratégia, o primeiro elemento com o nome de tag especificado será retornado. Se nenhum elemento tiver um nome de tag correspondente, um `` NoSuchElementException`` será gerado.

#### Exemplo teórico page source:  
```HTML
  <html>
   <body>
    <h1>Welcome</h1>
    <p>Site content goes here.</p>
  </body>
  <html>
```
A tag h1 pode ser localizado via tag name, como mostra abaixo:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  heading1 = driver.find_element_by_tag_name('h1')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### 8. Locating Elements by Class Name

Use quando desejar localizar um elemento pelo nome da classe. Com essa estratégia, o primeiro elemento com o atributo de nome de classe correspondente será retornado. Se nenhum elemento tiver um atributo de nome de classe correspondente, um `` NoSuchElementException`` será gerado.

For instance, consider this page source::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  <html>
   <body>
    <p class="content">Site content goes here.</p>
  </body>
  <html>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
O elemento "p" pode ser localizado via class name, como mostra abaixo:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  content = driver.find_element_by_class_name('content')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Sites de Treinamento (Treine nos sites abaixo):**  
http://automationpractice.com/index.php  
http://webdriveruniversity.com/index.html  
https://www.phptravels.net/index.php  
http://the-internet.herokuapp.com/  
http://newtours.demoaut.com/  
https://demoqa.com/  
https://ultimateqa.com/automation/  
https://www.saucedemo.com/  
https://automacaocombatista.herokuapp.com/  

**Referências (Este tópico foi somente traduzido para o português, os sites oficias se encontram abaixo):**  
https://selenium.dev/documentation/en/getting_started/  
https://selenium-python.readthedocs.io/locating-elements.html  
