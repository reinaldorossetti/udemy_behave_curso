from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, title_contains, title_is

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
        self.MSN = (By.ID, "msn")

    def find(self, *locator, timeout=10):
        try:
            result = WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))
            return result
        except:
            return False

    def login(self, user, password, value):
        status = self.find(self.NOME)
        if status:
            self.find(self.NOME).send_keys(user)
            self.find(self.PASS).send_keys(password)
            self.find(self.SUBMIT).click()
        else:
            print("Login jah efetuado...")
            elem = self.find(self.MSN)
            assert value in elem.text


driver = webdriver.Chrome()
driver.get("http://localhost:8083/html/login_feito.html")
test = LoginIn(driver)
test.login("Reinaldo", "12345", "Bem-Vindo Ao Sistema")
driver.quit()
