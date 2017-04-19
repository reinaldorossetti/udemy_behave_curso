# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep
from esperas import fluentwait


class TestInserirComentario(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # Seta um timeout pra pagina carregar
        #self.driver.set_page_load_timeout(10)
        self.base_url = "https://servicossociais.caixa.gov.br/internet.do?segmento=CIDADAO01&produto=FGTS"

    def test01_implict(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("vida de testador")
        # Espera pelo Python
        sleep(15)
        # Implicita Espera.
        driver.implicitly_wait(15)
        driver.find_element_by_xpath("//h3/a[contains(@href, 'reinaldorossetti')]").click()
        driver.find_element_by_link_text(u"Criando uma Mini-Interface para Execução de Scripts em Python").click()
        test = driver.find_element_by_css_selector("h3.post-title.entry-title").is_displayed()
        assert(test)

    def test02_explicit(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("vida de testador")

        elemento = fluentwait(self.driver, "//h3/a[contains(@href, 'reinaldorossetti')]",15)
        elemento.click()

        driver.find_element_by_link_text(u"Criando uma Mini-Interface para Execução de Scripts em Python").click()
        test = driver.find_element_by_css_selector("h3.post-title.entry-title").is_displayed()
        assert (test)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
