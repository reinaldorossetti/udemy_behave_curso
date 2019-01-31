from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \

    invisibility_of_element_located, title_contains, title_is


class BaixarPV:

    def __init__(self, firefox):

        self.browser = firefox

        self.click1 = (By.ID, 'login-home-btn')

        self.name = (By.ID, 'username')

        self.passw = (By.ID, 'senha')

        self.submit = (By.ID, 'menu-login')

       

    def find(self, *locator, timeout=30):

        return WebDriverWait(self.browser, timeout).until(visibility_of_element_located(*locator))

   

    def login(self, user, password):

        self.find(*self.click1).click()

        self.find(*self.name).send_keys(user)

        self.find(*self.passw).send_keys(password)

        self.find(*self.submit).click()

       

firefox = webdriver.Firefox()

firefox.get('https://tiny.com.br')

acao = BaixarPV(firefox)

acao.login = ('****','*****')
