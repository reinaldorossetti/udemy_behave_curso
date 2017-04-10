from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Instanciando o firefox driver.
# Passamos o caminho do driver, no meu caso eh linux a barra / eh no windows eh o contrario.
driver = webdriver.Chrome()
# Abre a url.
driver.get("http://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_node_firstchild")
# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(10)
# Muda para o frame correto.
driver.switch_to.frame("iframeResult")


def espera_explicita(driver, selector, delay=30):
    # Espera Explicita > Melhor forma de fazer.
    # An expectation for checking that an element is present on the DOM of a page and visible.
    return WebDriverWait(driver, delay).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))


espera_explicita(driver, "#myList")

# Procura o elemento na tela via CSS Selector.
elemento = driver.find_element(By.CSS_SELECTOR, "#myList")

element_father = elemento.get_property('firstElementChild')
first = elemento.get_property('firstElementChild')
last = elemento.get_property('lastElementChild')

# pegando o valor das propriedades da DOM dos elementos.
print(first.get_attribute('innerText'), last.get_attribute('innerText'))
print(first.get_attribute('outerHTML'), last.get_attribute('outerHTML'))
print(first.get_attribute('tagName'), last.get_attribute('tagName'))
print(element_father.get_attribute('baseURI'))

# Fazendo os assert, se os valores sao diferentes do esperado o assert vai falhar ou
# seja nosso teste falhou.

assert "Coffee" == first.get_attribute('innerText')
assert "Tea" == last.get_attribute('innerText')

# fecha o browser
driver.close()