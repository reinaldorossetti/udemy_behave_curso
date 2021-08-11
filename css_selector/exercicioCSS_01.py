
# importa as bibliotecas
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys



# instancio o driver do chrome
global driver
driver = webdriver.Chrome()

# navegar na url
driver.get("https://www.itau.com.br/")

driver.implicitly_wait(10)
driver.set_page_load_timeout(10)

# localizando o elemento
element01 = driver.find_element(By.CSS_SELECTOR, "a[class^=\"varejo\"][href*=empresas]")

element01.click()

elementoAgencia = driver.find_element(By.CSS_SELECTOR, "#agencia")

elementoAgencia.send_keys("3086")

elementoConta = driver.find_element(By.CSS_SELECTOR, "#conta")

elementoConta.send_keys("03171-7")

elementoBotaoConfirmar = driver.find_element(By.CSS_SELECTOR, "#btnLoginSubmit[class*=\"send active\"]")

elementoBotaoConfirmar.click()
#elementoBotaoConfirmar.send_keys(Keys.ENTER)

elementoMsnTexto = driver.find_element(By.CSS_SELECTOR, "#content h1[class*=margem-esquerda]")

# imprime o texto que esta contigo no meu elemento.
print(elementoMsnTexto.text)

# nosso assert, que valida se o teste esta correto
assert "Guardião Itaú 30 horas" == elementoMsnTexto.text

sleep(10)  # somente pra ver o resultado.

# fechar a tela
driver.quit()
