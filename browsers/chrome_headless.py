# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from global_page import Global_Page
from os import path

# Ao usar o modo headless tem que prestar atencao na versao do browser, cada driver suporta a versao especificada determinada por eles.
# exemplo driver 77 suporta no maximo a versao 77 do browser do chrome, ou seja superior a isso vai dar erro.
# https://chromedriver.chromium.org/downloads

class CadastrarConta(Global_Page):

    def __init__(self, driver):
        self.driver = driver
        self.NOME = (By.NAME, "firstname")
        self.LASTNAME = (By.NAME, "lastname")
        self.EMAIL = (By.NAME, "reg_email__")
        self.EMAIL_CONFIRM = (By.NAME, "reg_email_confirmation__")
        self.PASS = (By.NAME, "reg_passwd__")
        self.SEXO = (By.CSS_SELECTOR, "#reg_form_box label")
        self.DIA = (By.NAME, "birthday_day")
        self.MES = (By.NAME, "birthday_month")
        self.ANO = (By.NAME, "birthday_year")
        self.SUBMIT = (By.CSS_SELECTOR, "button[type=submit]")

    def test_cadastrar_user_facebook(self, dados_user):
        self.preencher_dados(dados_user['nome'], dados_user['sobrenome'], dados_user['email'],
                                                                                     dados_user['senha'])
        self.label_click(dados_user['sexo'])
        self.data_de_nascimento(dados_user['data_nascimento'])
        self.find(self.SUBMIT).click()

    def preencher_dados(self, nome, sobrenome, email, senha):
        self.find(self.NOME).send_keys(nome)
        self.find(self.LASTNAME).send_keys(sobrenome)
        self.find(self.EMAIL).send_keys(email)
        self.find(self.PASS).send_keys(senha)
        self.find(self.EMAIL_CONFIRM).send_keys(email)

    def label_click(self, sexo):
        for x in self.find_all(self.SEXO):
            if x.text == sexo: x.click()

    def data_de_nascimento(self, data_nascimento):
        dia, mes, ano = data_nascimento.split("/")
        Select(self.find(self.DIA)).select_by_value(str(dia))
        Select(self.find(self.MES)).select_by_value(str(mes))
        Select(self.find(self.ANO)).select_by_value(str(ano))


# faz a instancia do driver em modo headless
chrome_options = Options()
chrome_options.add_argument("start-maximized")
#chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox") # linux admin permisao.
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="./drivers/chromedriver77.exe", options=chrome_options)

# inicia o browser
driver.get("https://www.facebook.com/")
test = CadastrarConta(driver)
dados_user = {
    'nome': "Reinaldo",
    'sobrenome': "Mateus",
    'email': "reiload@gmail.com",
    'senha':"Rei12345",
    'data_nascimento': "3/10/1980",
    'sexo': "Masculino"
}
test.test_cadastrar_user_facebook(dados_user)
ROOT_DIR = path.dirname(path.abspath(__file__)) + "/test_headless.png"
print(ROOT_DIR)
driver.save_screenshot(ROOT_DIR)
driver.quit()
