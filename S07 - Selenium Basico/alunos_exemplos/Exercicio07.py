from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/radio_exemplo.html
"""
global driver
driver = webdriver.Chrome()

driver.get("http://localhost:8083/html/radio_exemplo.html")
CSS = (By.ID, "css")
AGE3 = (By.ID, "age3")


def find(*locator):
    return WebDriverWait(driver, 15).until(visibility_of_element_located(locator))


elemento01 = find(*CSS).click()
elemento02 = find(*AGE3).click()

# Gets the given attribute or property of the element.
elemento01_apos = find(*AGE3)
valor01 = elemento01_apos.get_attribute("value")
valor02 = elemento01_apos.get_attribute("id")
AGE_VALUE = (By.CSS_SELECTOR, "label[for=" + valor02 + "]")

print(valor01)
print(valor02)
# verifica se o elemento foi selecionado
print(elemento01_apos.is_selected())
# verifica se o elemento esta visivel
print(elemento01_apos.is_displayed())
# verifica se o elemento esta habilitado
print(elemento01_apos.is_enabled())

elemento_label = find(*AGE_VALUE)
# pegando a propriedade texto do elemento
valor03 = elemento_label.get_property("textContent")
print(valor03)
assert "61 - 100" == valor03

sleep(10)  # somente pra ver o resultado.
driver.quit()
