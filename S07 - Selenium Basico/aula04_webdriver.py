from selenium import webdriver
from selenium.webdriver.common.by import By
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""

driver = webdriver.Chrome()
# em caso de falha por não localizar o elemento, descomente a linha abaixo.
# driver.implicitly_wait(30)

NOME = (By.ID, "name123")
PASS = (By.ID, "pass123")
SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
RESULT = (By.CSS_SELECTOR, "div.w3-border")

driver.get("http://localhost:8083/html/login.html")


def login(user, password):

    driver.find_element(*NOME).send_keys(user)

    driver.find_element(*PASS).send_keys(password)

    driver.find_element(*SUBMIT).click()

    elem = driver.find_element(*RESULT)

    assert "uname=Reinaldo&psw=12345" in elem.text

login("Reinaldo", "12345")

driver.quit()
