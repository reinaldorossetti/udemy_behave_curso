# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, presence_of_all_elements_located


# classe que contem as funçoes globais.

class Global_Page():

    def __init__(self, driver):
        self.driver = driver
        self.el = None

    def time_max(self):
        timeout = 35
        return timeout

    def find_all(self, *locator):
        try:
            self.el = WebDriverWait(self.driver, self.time_max()).until(presence_of_all_elements_located(*locator))
        except Exception as ex:
            print (ex)
        return self.el

    def find(self, *locator):
        try:
            self.el = WebDriverWait(self.driver, self.time_max()).until(visibility_of_element_located(*locator))
        except Exception as ex:
            print (ex)
        return self.el

    def find_not(self, *locator):
        try:
            self.el = WebDriverWait(self.driver, self.time_max()).until(invisibility_of_element_located(*locator))
        except Exception as ex:
            print (ex)
        return self.el

    def tearDown(self):
        self.driver.quit()
