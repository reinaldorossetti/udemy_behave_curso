from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, presence_of_all_elements_located


# classe que contém as funções globais.

class GlobalPage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 35

    def find_all(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(presence_of_all_elements_located(*locator))

    def find(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(visibility_of_element_located(*locator))

    def find_not(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(invisibility_of_element_located(*locator))

    def tearDown(self):
        self.driver.quit()
