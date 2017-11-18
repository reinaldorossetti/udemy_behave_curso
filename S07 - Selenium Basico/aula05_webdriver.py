from selenium import webdriver
from selenium.webdriver.common.by import By
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""


class LoginIn:

    def __init__(self, driver):
        self.driver = driver
        self.NOME = (By.ID, "name123")
        self.PASS = (By.ID, "pass123")
        self.SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
        self.RESULT = (By.CSS_SELECTOR, "div.w3-border")

    def login(self, user, password):

        driver.find_element(*self.NOME).send_keys(user)

        driver.find_element(*self.PASS).send_keys(password)

        driver.find_element(*self.SUBMIT).click()

    def validar(self, value):

        elem = driver.find_element(*self.RESULT)

        assert value in elem.text


driver = webdriver.Chrome()
driver.get("http://localhost:8083/html/login.html")
test = LoginIn(driver)
test.login("Reinaldo", "12345")
test.validar("uname=Reinaldo&psw=12345")
driver.quit()
