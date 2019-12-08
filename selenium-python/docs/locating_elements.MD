### Métodos para localizar elementos:

Existem várias estratégias para localizar elementos em uma página. Você pode usar o mais apropriado para o seu caso. 
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
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com.br")

driver.find_element(By.XPATH, '//input[@value="Pesquisa Google"]')
driver.find_elements(By.XPATH, '//input')

driver.find_element(By.CSS_SELECTOR, 'input[value="Pesquisa Google"]')
driver.find_elements(By.CSS_SELECTOR, 'input')
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

ao invés de localizar os elementos via By, podemos fazer isso diretamente, exemplo:

```
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com.br")

driver.find_element_by_xpath('//input[@value="Pesquisa Google"]')
driver.find_elements_by_xpath('//input') # somente acrescenta o s em element.

driver.find_element_by_css_selector('input[value="Pesquisa Google"]')
driver.find_elements_by_css_selector('input[value="Pesquisa Google"]')
```

### 2. Localizando elementos por Id (é sempre a melhor opção de localização)

Use isso quando tiver o atributo `id` em um elemento. Com isso
estratégia, o primeiro elemento com o atributo `id` correspondente
é retornado. Se nenhum dos elementos da pagina não tiver nenhum atributo `id` correspondente,
vai retornar um erro `` NoSuchElementException`` o erro será gerado.

~~~~~~~~~~~~~~
# For instance, consider this page source::

  <html>
   <body>
    <form id="loginForm">
     <input name="username" type="text" />
     <input name="password" type="password" />
     <input name="continue" type="submit" value="Login" />
    </form>
   </body>
  <html>

# The form element can be located like this::

  login_form = driver.find_element_by_id('loginForm')

~~~~~~~~~~~~~~~~

### 3. Localizando elemento por Name

Use quando tiver o atributo name de um elemento. Com essa estratégia, o primeiro elemento com um atributo de nome correspondente será retornado. Se nenhum elemento tiver um atributo de nome correspondente, será gerado um NoSuchElementException.

~~~~~~~~~~~~~~~~
# For instance, consider this page source::

   <html>
    <body>
     <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
     </form>
   </body>
   <html>

# The username & password elements can be located like this::

  username = driver.find_element_by_name('username')
  password = driver.find_element_by_name('password')

# This will give the "Login" button as it occurs before the "Clear"
# button::

  continue = driver.find_element_by_name('continue')

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### 4. Localizando elemento por CSS Selectors

Use this when you want to locate an element using CSS selector syntax.
With this strategy, the first element matching the given CSS selector
will be returned.  If no element matches the provided CSS selector,
a ``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p class="content">Site content goes here.</p>
  </body>
  <html>

The "p" element can be located like this::

  content = driver.find_element_by_css_selector('p.content')

`Sauce Labs has good documentation <https://saucelabs.com/resources/articles/selenium-tips-css-selectors>`_
on CSS selectors.


### 5. Localizando elemento por by XPath
~~~~~~~~~~~~~~~~~

XPath is the language used for locating nodes in an XML document.  As
HTML can be an implementation of XML (XHTML), Selenium users can
leverage this powerful language to target elements in their web
applications.  XPath supports the simple methods of locating by 
id or name attributes and extends them by opening up all sorts
of new possibilities such as locating the third checkbox on the page.

One of the main reasons for using XPath is when you don't have a
suitable id or name attribute for the element you wish to locate.  You
can use XPath to either locate the element in absolute terms (not
advised), or relative to an element that does have an id or name
attribute.  XPath locators can also be used to specify elements via
attributes other than id and name.

Absolute XPaths contain the location of all elements from the root
(html) and as a result are likely to fail with only the slightest
adjustment to the application.  By finding a nearby element with an id
or name attribute (ideally a parent element) you can locate your
target element based on the relationship.  This is much less likely to
change and can make your tests more robust.

For instance, consider this page source::

   <html>
    <body>
     <form id="loginForm">
      <input name="username" type="text" />
      <input name="password" type="password" />
      <input name="continue" type="submit" value="Login" />
      <input name="continue" type="button" value="Clear" />
     </form>
   </body>
   <html>

The form elements can be located like this::

  login_form = driver.find_element_by_xpath("/html/body/form[1]")
  login_form = driver.find_element_by_xpath("//form[1]")
  login_form = driver.find_element_by_xpath("//form[@id='loginForm']")


1. Absolute path (would break if the HTML was changed only slightly)

2. First form element in the HTML

3. The form element with attribute `id` set to `loginForm`

The username element can be located like this::

  username = driver.find_element_by_xpath("//form[input/@name='username']")
  username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
  username = driver.find_element_by_xpath("//input[@name='username']")

1. First form element with an input child element with `name` set to `username`

2. First input child element of the form element with attribute `id` set to `loginForm`

3. First input element with attribute `name` set to `username`

The "Clear" button element can be located like this::

  clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
  clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")


1. Input with attribute `name` set to `continue` and
   attribute `type` set to `button`

2. Fourth input child element of the form element with attribute `id` set to `loginForm`

These examples cover some basics, but in order to learn more, the
following references are recommended:

* `W3Schools XPath Tutorial <https://www.w3schools.com/xml/xpath_intro.asp>`_
* `W3C XPath Recommendation <http://www.w3.org/TR/xpath>`_
* `XPath Tutorial
  <http://www.zvon.org/comp/r/tut-XPath_1.html>`_
  - with interactive examples.

There are also a couple of very useful Add-ons that can assist in
discovering the XPath of an element:

* `XPath Checker
  <https://addons.mozilla.org/en-US/firefox/addon/xpath-checker/>`_ -
  suggests XPath and can be used to test XPath results.
* `Firebug <https://addons.mozilla.org/en-US/firefox/addon/firebug/>`_ -
  XPath suggestions are just one of the many powerful features of this
  very useful add-on.
* `XPath Helper
  <https://chrome.google.com/webstore/detail/hgimnogjllphhhkhlmebbmlgjoejdpjl>`_ -
  for Google Chrome


Locating Hyperlinks by Link Text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you know the link text used within an anchor tag. With this
strategy, the first element with the link text matching the provided value 
will be returned.  If no element has a matching link text
attribute, a ``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p>Are you sure you want to do this?</p>
    <a href="continue.html">Continue</a>
    <a href="cancel.html">Cancel</a>
  </body>
  <html>

The continue.html link can be located like this::

  continue_link = driver.find_element_by_link_text('Continue')
  continue_link = driver.find_element_by_partial_link_text('Conti')


Locating Elements by Tag Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you want to locate an element by tag name. With this
strategy, the first element with the given tag name will be returned.
If no element has a matching tag name, a ``NoSuchElementException``
will be raised.

For instance, consider this page source::

  <html>
   <body>
    <h1>Welcome</h1>
    <p>Site content goes here.</p>
  </body>
  <html>

The heading (h1) element can be located like this::

  heading1 = driver.find_element_by_tag_name('h1')


Locating Elements by Class Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use this when you want to locate an element by class name.
With this strategy, the first element with the matching class name 
attribute will be returned.  If no element has a matching class name attribute,
a ``NoSuchElementException`` will be raised.

For instance, consider this page source::

  <html>
   <body>
    <p class="content">Site content goes here.</p>
  </body>
  <html>

The "p" element can be located like this::

  content = driver.find_element_by_class_name('content')

