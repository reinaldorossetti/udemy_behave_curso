from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, title_contains, title_is
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""


class IframeSample:

    def __init__(self, driver):
        self.driver = driver
        self.RUN = (By.ID, "run")
        self.EXPANDIR = (By.CSS_SELECTOR, "small a[href*=\"google\"]")
        self.HOME = (By.CSS_SELECTOR, "a[title=\"JSFiddle\"]")
        self.EMPTY = (By.CSS_SELECTOR, "a[href=\"/\"]")

    def find(self, *locator, timeout=20):
        return WebDriverWait(driver, timeout).until(visibility_of_element_located(*locator))

    def find_not(self, *locator, timeout=20):
        return WebDriverWait(driver, timeout).until(invisibility_of_element_located(*locator))

    def title_contains(self, *locator, timeout=20):
        return WebDriverWait(driver, timeout).until(title_contains(*locator))

    def run(self):
        self.find(self.RUN).click()

    def expandir(self):
        self.driver.switch_to.frame("result")
        self.find(self.EXPANDIR).click()

    def page_principal(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.default_content()
        self.find(self.HOME).send_keys(Keys.ENTER)
        self.find(self.EMPTY).send_keys(Keys.ENTER)

    def validar(self, url):
        assert self.driver.current_url == url


driver = webdriver.Chrome()
driver.get("https://jsfiddle.net/4b58ah85/7/")
driver.maximize_window()
test = IframeSample(driver)
test.run()
test.expandir()
test.page_principal()
test.validar("https://jsfiddle.net/4b58ah85/7/")
driver.quit()
