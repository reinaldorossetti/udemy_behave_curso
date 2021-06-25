from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""

driver = webdriver.Chrome()
driver.get("http://localhost:8083/html/radio_exemplo.html")
CSS = (By.ID, "css")
AGE3 = (By.ID, "age3")

elemento01 = driver.find_element(*CSS).click()
elemento02 = driver.find_element(*AGE3).click()

# Gets the given attribute or property of the element.
elemento01_apos = driver.find_element(*AGE3)
valor01 = elemento01_apos.get_attribute("value")
valor02 = elemento01_apos.get_attribute("id")
AGE_VALUE = (By.CSS_SELECTOR, "label[for="+valor02+"]")

print(valor01)
print(valor02)
# verifica se o elemento foi selecionado
print(elemento01_apos.is_selected())
print(elemento01_apos.is_displayed())
print(elemento01_apos.is_enabled())

elemento_label = driver.find_element(*AGE_VALUE)
valor03 = elemento_label.get_property("textContent")
print(valor03)
assert "61 - 100" == valor03

sleep(10) # somente pra ver o resultado.
driver.quit()

