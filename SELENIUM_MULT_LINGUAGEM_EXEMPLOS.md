Na pasta exemplo_selenium_mult_linguagem, vamos comparar as linguagens fazendo um teste simples.

### Vamos primeiro analisar a quantidade de caracteres sem os espaços:
<br>Java > 467 caracteres.
<br>C# > 387 caracteres.
<br>JavaScript > 371 caracteres.
<br>Ruby > 228 caracteres.
<br>Python > 207 caracteres.

Analisando os exemplos acima Java é a linguagem mais verbosa, seguindo por c#, as duas linguagens te obriga a programar orientado a objetos, as outras no entanto não, posso fazer o script sem ter a obrigação de programar orientado a objetos. 

Temos que entender que nem sempre você precisa criar classes, não faz sentido criar classes sem ter objetos que sejam compartilhados entre os métodos, como nesse caso de um simples teste.


Vamos dissecar o nosso Script de Teste agora:

#### 1. A primeira coisa de devemos fazer é importar a biblioteca do selenium.
Em python fazemos:<br>
<b><i> from selenium import webdriver</i></b><br>
Em ruby fazemos:<br>
<b><i> require "selenium-webdriver"</i></b>

#### 2. A segunda coisa que devemos fazer é instanciar a biblioteca do selenium, não basta importar a biblioteca, temos que instanciar a mesma.<br>
Em python fazemos:<br>
<b><i> driver = webdriver.Firefox()</i></b><br>
Em ruby fazemos:<br>
<b><i> driver = Selenium::WebDriver.for :firefox</i></b>

É bem similar nas duas linguagens, mas a sintax muda de linguagem para linguagem, em java e C# temos o uso do <b>new</b> e é preciso declarar o tipo do objeto. Exemplo: <i>WebDriver driver = new FirefoxDriver();</i>
<br><br>Pra que eu preciso instanciar a biblioteca?<br>
Sem instanciar a biblioteca/framework do selenium você não consegue ter acesso ao métodos/funções que a biblioteca disponibilizar.


#### 3. A primeira coisa que você precisa fazer no seu teste é navegar para uma página, para isso com o Selenium WebDriver é preciso chamar a função "get", em C# usa a função "Url" e em Ruby usa o "navigate.to":
Em python fazemos:<br>
<b><i> driver.get("http://www.google.com")</i></b><br>
Em ruby fazemos:<br>
<b><i> driver.navigate.to "http://www.google.com"</i></b>

#### 4. Após carregar a página no browser, temos que localizar o elemento no browser, isso é feito através dos metódos "Find Element" ou "Find Elements", no primeiro método ele traz somente um WebElement, no segundo método ele traz uma lista de WebElement. Vejo muitos erros de a pessoa usar o método "Find Elements" e tenta usar como se fosse o "Find Element", um elemento é diferente de uma lista.
Em python fazemos:<br>
<b><i> element = driver.find_element_by_name("q")</i></b><br>
ou usando a classe By no python:<br>
<b><i> element = driver.find_element(By.ID, 'q')</i></b><br>
Em ruby fazemos:<br>
<b><i> element = driver.find_element(:name, 'q')</i></b>

** Usando a classe By temos que fazer o seguinte import:<br>
from selenium.webdriver.common.by import By
> Gosto de usar o find_element(By.ID, 'q'), pois ele é um método genérico, faço a função e passo o locator para dentro dele.
