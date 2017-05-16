# -*- coding: utf-8 -*-
# importando a biblioteca do selenium.
from selenium import webdriver

# Instanciando o driver do firefox, o geckodriver deve estar no path do SO ou na pasta Scripts.
driver = webdriver.Firefox()

# url do facebook
base_url = "https://www.facebook.com/"

# Carrega a url no browser.
driver.get(self.base_url + "/")

# Espera implicita de 60 segundos para carregar os elementos na url.
driver.implicitly_wait(60)

# Procura o elemento web pelo id email.
elem01 = driver.find_element_by_id("email")
# vai limpar o campo web email, antes de enviar o texto.
elem01.clear()
# vai enviar o texto para o nosso primeiro elemento.
elem01.send_keys("teste")

# Procura o elemento web pelo id pass.
elem02 = driver.find_element_by_id("pass")
# vai limpar o campo web password, antes de enviar o texto.
elem02.clear()
# vai enviar o texto para o nosso segundo elemento.
elem02.send_keys("teste")

# traz o elemento web via css e dar o click.
driver.find_element_by_css_selector("#loginbutton input[type='submit']").click()
