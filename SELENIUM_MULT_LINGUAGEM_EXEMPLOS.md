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
<b><i> from selenium import webdriver</i></b>
Em ruby fazemos:<br>
<b><i> require "selenium-webdriver"</i></b>

#### 2. A segunda coisa que devemos fazer é instanciar a biblioteca do selenium, não basta importar a biblioteca, temos que instanciar a mesma.<br>
Em python fazemos:<br>
<b><i> driver = webdriver.Firefox()</i></b>
Em ruby fazemos:<br>
<b><i> driver = Selenium::WebDriver.for :firefox</i></b>

É bem similar nas duas linguagens, mas a sintax muita de linguagem para linguagem, em java e C# temos o uso do <b>new</b> e é preciso declarar o tipo do objeto. Exemplo: <i>WebDriver driver = new FirefoxDriver();</i><br>
Pra que eu preciso instanciar a biblioteca?<br> Sem instanciar a biblioteca/framework do selenium você não consegue ter acesso ao métodos/funções que a biblioteca disponibilizar.
