from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Instanciando o firefox driver.
# Passamos o caminho do driver, no meu caso eh linux a barra / eh no windows eh o contrario.
driver = webdriver.Firefox()
driver.set_window_position(2000, 0)
# Abre a url.
driver.get("http://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_node_firstchild")
# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(30)
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

# innerHTML vai pegar o que estah contido dentro do elemento id=myList
# <ul id="myList"><li>Coffee</li><li>Tea</li></ul>
print(elemento.get_attribute('innerText'))
# Meus asserts pra saber se o teste foi realizado com sucesso.
assert "Coffee" in elemento.get_attribute('innerText')
assert "Tea" in elemento.get_attribute('innerHTML')

# fecha o browser
driver.quit()
