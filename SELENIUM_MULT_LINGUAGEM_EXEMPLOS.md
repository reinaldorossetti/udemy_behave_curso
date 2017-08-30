Na pasta exemplo_selenium_mult_linguagem, vamos comparar as linguagens fazendo um teste simples.

### Vamos primeiro analisar a quantidade de caracteres sem os espaços:
<br>Java > 467 caracteres.
<br>C# > 387 caracteres.
<br>JavaScript > 371 caracteres.
<br>Ruby > 228 caracteres.
<br>Python > 216 caracteres.

Analisando os exemplos acima Java é a linguagem mais verbosa, seguindo por c#, as duas linguagens te obriga a programar orientado a objetos, as outras no entanto não, posso fazer o script sem ter a obrigação de programar orientado a objetos. 

Temos que entender que nem sempre você precisa criar classes, não faz sentido criar classes sem ter objetos que sejam compartilhados entre os métodos, como nesse caso de um simples teste.


Vamos dissecar o nosso Script de Teste agora:

#### 1. A primeira coisa de devemos fazer é importar a biblioteca do selenium.
Em python fazemos:<br>
<b><i> from selenium import webdriver</i></b><br>
Em ruby fazemos:<br>
<b><i> require "selenium-webdriver"</i></b><br>
Em java fazemos:<br>
<b><i> import org.openqa.selenium.By;<br>
import org.openqa.selenium.WebDriver;<br>
import org.openqa.selenium.WebElement;<br>
import org.openqa.selenium.firefox.FirefoxDriver;</i></b>

#### 2. A segunda coisa que devemos fazer é instanciar a biblioteca do selenium, não basta importar a biblioteca, temos que instanciar a mesma.<br>
Em python fazemos:<br>
<b><i> driver = webdriver.Firefox()</i></b><br>
Em ruby fazemos:<br>
<b><i> driver = Selenium::WebDriver.for :firefox</i></b><br>
Em java fazemos:<br>
<b><i> WebDriver driver = new FirefoxDriver();</i></b>

É bem similar nas duas linguagens, mas a sintax muda de linguagem para linguagem, em java e C# temos o uso do <b>new</b> e é preciso declarar o tipo do objeto. Exemplo: <i>WebDriver driver = new FirefoxDriver();</i>
<br><br>Pra que eu preciso instanciar a biblioteca?<br>
Sem instanciar a biblioteca/framework do selenium você não consegue ter acesso ao métodos/funções que a biblioteca disponibilizar.


#### 3. A primeira coisa que você precisa fazer no seu teste é navegar para uma página, para isso com o Selenium WebDriver é preciso chamar a função "get", em C# usa a função "Url" e em Ruby usa o "navigate.to":
Em python fazemos:<br>
<b><i> driver.get("http://www.google.com")</i></b><br>
Em ruby fazemos:<br>
<b><i> driver.navigate.to "http://www.google.com"</i></b><br>
Em Java fazemos:<br>
<b><i> driver.get("http://www.google.com");</i></b><br>

#### 4. Após carregar a página no browser, temos que localizar o elemento no browser, isso é feito através dos metódos "Find Element" ou "Find Elements", no primeiro método ele traz somente um WebElement, no segundo método ele traz uma lista de WebElement. Vejo muitos erros de a pessoa usar o método "Find Elements" e tenta usar como se fosse o "Find Element", um elemento é diferente de uma lista.
Em python fazemos:<br>
<b><i> element = driver.find_element_by_name("q")</i></b><br>
ou usando a classe By no python:<br>
<b><i> element = driver.find_element(By.ID, 'q')</i></b><br>
Em ruby fazemos:<br>
<b><i> element = driver.find_element(:name, 'q')</i></b><br>
Em java fazemos:<br>
<b><i> WebElement element = driver.findElement(By.name("q"));</i></b>

** Usando a classe By temos que fazer o seguinte import:<br>
from selenium.webdriver.common.by import By
> Gosto de usar o find_element(By.ID, 'q'), pois ele é um método genérico, faço a função e passo o locator para dentro dele.

#### 5. Após localizar o elemento que desejamos, precisamos efetuar alguma ação sobre ele, uma das ações é enviar um texto para um campo do tipo input. Para isso temos que usar o método "Send Keys".
Em python fazemos:<br>
<b><i> element.send_keys("Hello Selenium WebDriver!")</i></b><br>
Em ruby fazemos:<br>
<b><i> element.send_keys "Hello Selenium WebDriver!"</i></b><br>
Em java fazemos:<br>
<b><i> element.sendKeys("Hello Selenium WebDriver!");</i></b>

** No Python 3 eu preciso usar os parênteses (), no python 2 você não precisa usar os parênteses, ficaria igual ao ruby.

#### 6. Após enviar o texto para o campo, para efetuar a busca no formulário precisamos efetuar o submit, o submit faz com que o formulário processe a ação, no caso do form do campo busca do google a ação é action="/search".
Em python fazemos:<br>
<b><i> element.submit()</i></b><br>
Em ruby fazemos:<br>
<b><i> element.submit</i></b><br>
Em java fazemos:<br>
<b><i> element.submit();</i></b>

** No Java, C#, JavaScript é sempre preciso colocar o ponto e vírgula no final do comando.


#### 7. Por fim ele vai imprimir o título da página HTML.
Em python fazemos:<br>
<b><i> print(driver.title)</i></b><br>
Em ruby fazemos:<br>
<b><i> puts driver.title</i></b><br>
Em java fazemos:<br>
<b><i> System.out.println(driver.getTitle());</i></b>


Em empresa que tem fábrica de automação de testes, ou seja dão manutenção em diversos projetos com linguagens diferentes. É super importante conhecer o básico das linguagens e as diferenças do Selenium em cada linguagem. 

Analisando Ruby e Python tem os mesmos conceitos ágil, a sintax é muito similar, o que gosto muito de python é que a linguagem segue uma filosofia bem definida, no entanto em ruby tem uma quantidade de frameworks bem mais maduros como capybara e watir que não tem para python até o momento.

Para quem está començando a mexer e não domina a linguagem um framework é uma mão na roda, mas pra quem domina a linguagem sabe que um framework somente abstrai os métodos para o usuário, e deixa eles de forma fácil de mexer, em alguns pontos pode ser ruim por não ser flexível, pois o mesmo segue um conjunto de regras. No entanto no dia a dia quanto você tem um quantidade de testes gigantes um framework ajuda muito, pois ainda diminui muito a quantidade de caracteres que analisamos acima, esse é um exemplo simples em um projeto gigante é muita diferença pra linguagens que tem o conceito ágil. 

Pontos pra Python:
- Possui Herança Multipla por padrão;
- Possui List Comprehensions, o seja em uma linha você consegue fazer muita coisa;
- Indentação de Código, não precisa colocar do e end do ruby ou {} do java pra iniciar e terminar um bloco de código.
- Python tudo é objeto internamente, ou seja na linguagem não precisa colocar new object/get/set do java.

Pontos do Ruby:
- Você consegue mandar vários comandos em uma linha;
- Possui frameworks maduros baseados no Selenium WebDriver;

**Observação não estou falando mal de Java e C#, só estou mostrando as facilidades das linguagens que tem a concepção ágil, em testes isso vai facilitar a sua vida! A demanda de testes é muito grande e quanto mais facilidades melhor é pra você.


**Vamos comparar com o selenium em java:**

``` Java
 @FindBy(id = "id_time_zone")
WebElement editSubOrg_timezone;

// Reads and returns field
  List<String> getAllOptions(By by) {
      List<String> options = new ArrayList<String>();
      for (WebElement option : new Select(driver.findElement(by)).getOptions()) {
          String txt = option.getText();
          if (option.getAttribute("value") != "") options.add(option.getText());
      }
      return options;
  } 

List<String> options = getAllOptions(editSubOrg_timezone);
System.out.println(options);

```

**Em Watir a mesma coisa:**
``` Ruby
  ELEM_SELECT = {id: "id_time_zone"}
  
  def select_list_text(locator_select)
    Watir::Wait.until { @driver.select_list(locator_select).options.length > 0}
    @driver.select_list(locator_select).options.map(&:text)
  end
  
  puts select_list_text(ELEM_SELECT)
```
**Sem dúvida em ruby com Watir é muito mais simples fazer, sem contar que a função está esperando o combobox ter valores, ou seja espera espera o options.length > 0 ser igual a true por 30 segundos.

Segue abaixo os dois principais frameworks em Ruby:<br>
https://github.com/reinaldorossetti/capybara_tips<br>
https://github.com/reinaldorossetti/watir_tips<br>

Referência: http://www.seleniumhq.org/docs/03_webdriver.jsp#introducing-webdriver
