from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.utils import keys_to_typing
import re
from selenium.webdriver.common.action_chains import ActionChains

"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://www.geradorcpf.com/mascara-cpf-com-jquery.htm
"""

# Instanciando o firefox driver.
driver = webdriver.Firefox()
# Abre a url.
driver.get("http://127.0.0.1:8083/html/cpf.html")

# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(30)


def find(driver, selector, delay=30):
    # Espera Explicita > Melhor forma de fazer.
    # An expectation for checking that an element is present on the DOM of a page and visible.
    return WebDriverWait(driver, delay).until(
        expected_conditions.visibility_of_element_located(("css selector", selector)))

elemento = find(driver, "input[id=cpf]")
print(elemento)

cpf = "52540430066"

driver.execute_script("arguments[0].value='" + cpf + "';", elemento)
driver.execute_script('$("#cpf").mask("999.999.999-99");')
# # Meus asserts pra saber se o teste foi realizado com sucesso.

elemento = find(driver, "input[id=cpf]")
value = elemento.get_attribute('value')
value = re.sub(r'(\D+)', '', value)

assert cpf in value

# fecha o browser
# driver.quit()
