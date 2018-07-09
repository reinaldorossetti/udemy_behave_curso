# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, presence_of_all_elements_located
from selenium.webdriver.support.ui import Select
from time import sleep
import elements.elements_page_cadastro_de_conta

# Pagina de Cadastro de Conta.

class CadastrarConta(elements.elements_page_cadastro_de_conta.CadastrarContaElements):

    def __init__(self, driver, page_global):
        self.driver = driver
        self.func = page_global

    def cadastro_facebook(self, nome, sobrenome, email, novasenha, data_nascimento, sexo):

        self.func.find(self.NOME).send_keys(nome)
        self.func.find(self.LASTNAME).send_keys(sobrenome)
        self.func.find(self.EMAIL).send_keys(email)
        self.func.find(self.PASS).send_keys(novasenha)
        self.func.find(self.EMAIL_CONFIRM).send_keys(email)
        self.label_click(sexo)
        self.data_de_nascimento(data_nascimento)
        self.func.find(self.SUBMIT).click()

    def label_click(self, sexo):
        for x in self.func.find_all(self.SEXO):
            if x.text == sexo: x.click()

    def data_de_nascimento(self, data_nascimento):
        dia, mes, ano = data_nascimento.split("/")
        Select(self.func.find(self.DIA)).select_by_value(str(dia))
        Select(self.func.find(self.MES)).select_by_value(str(mes))
        Select(self.func.find(self.ANO)).select_by_value(str(ano))


# classe que contém as funções globais.

class Global_Page():

    def __init__(self, driver):
        self.driver = driver

    def find_all(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(presence_of_all_elements_located(*locator))

    def find(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))

    def find_not(self, *locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(invisibility_of_element_located(*locator))

    def tearDown(self):
        self.driver.quit()

# faz a chamada de uma classe principal ou do step definition do behave.
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com/")
page_global = Global_Page(driver)
test = CadastrarConta(driver, page_global)
test.cadastro_facebook("Reinaldo", "Mateus", "reiload@gmail.com", "Rei12345", "3/10/1980", "Masculino")

sleep(10) # somente para mostra os dados cadastrados.
page_global.tearDown()
