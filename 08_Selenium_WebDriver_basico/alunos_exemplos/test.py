import requests
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver


def instaciar_driver():
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    caps["binary"] = "C:\Program Files\Mozilla Firefox\\firefox.exe "
    driver = webdriver.Firefox(capabilities=caps, executable_path="C:\Python35-32\Scripts\wires.exe")
    return driver


def carregando_url(driver, url):
    driver.set_page_load_timeout(30)
    driver.get(url)
    url = requests.get(url)
    print(url.status_code)
    return url.status_code

driver = instaciar_driver()
teste = carregando_url(driver, "http://reinaldorossetti.blogspot.com.br/")
assert teste == 200, "Erro ao carregar a pagina."
