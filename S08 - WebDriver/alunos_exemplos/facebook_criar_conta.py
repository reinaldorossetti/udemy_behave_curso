# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import elements.elements_page_cadastro_de_conta
import global_page

# Pagina de Cadastro de novo usuario no facebbok.
class CadastrarConta(global_page.Global_Page,
                     elements.elements_page_cadastro_de_conta.CadastrarContaElements):

    def __init__(self, driver):
        self.driver = driver

    def test_cadastrar_user_facebook(self, dados_user):
        self.preencher_dados(dados_user['nome'], dados_user['sobrenome'], dados_user['email'],
                                                                                     dados_user['senha'])
        self.label_click(dados_user['sexo'])
        self.data_de_nascimento(dados_user['data_nascimento'])
        sleep(5) # somente para mostra os dados cadastrados.
        self.find(self.SUBMIT).click()
        self.tearDown()

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

# faz a chamada de uma classe principal ou do step definition do behave.
driver = webdriver.Firefox()
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
