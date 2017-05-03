from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
"""

# instanciamos o driver do chrome.
driver = webdriver.Chrome()
# deixamos a tela no modo tela cheia.
driver.maximize_window
# windows path - carrega a url.
driver.get("http://127.0.0.1:8083/html/prompt.html")

# nosso funcao de espera do pop-up.
def wait_alert(time=15):
    element = WebDriverWait(driver, time).until(alert_is_present())
    return element

# linux path
# driver.get("http://127.0.0.1:8083/alert_tests/html/prompt.html")
# fazemos uma espera implicita
driver.implicitly_wait(10)

# localizado o elemento button.
test = driver.find_element("id","prompt")

# damos o click no botao.
test.click()

# chamamos a nossa funcao de espera.
alert = wait_alert()

# pegamos o texto da janela de dialogo e mostramos no console.
print(alert.text)

# enviamos o texto e damos ok no botao.
nome = "Reinaldo Mateus"
alert.send_keys(nome)
alert.accept()

# validamos os dados.
test2 = driver.find_element("id", "demo")
result = driver.execute_script("return test")
print(result, test2.text)
assert test2.text == nome

# saimos do browser.
driver.quit()
