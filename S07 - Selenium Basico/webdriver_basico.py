# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class WebDriver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://reinaldorossetti.blogspot.com.br"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_webdriver(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_class_name(".gsc-search-box [class*=\"gsc-input\"]").clear()
        driver.find_element_by_css_selector(".gsc-search-box [class*=\"gsc-input\"]").send_keys(
            u"testes de segurança")

        # print (driver.title)
        # print(driver.name)
        # print(driver.current_url)
        # print(driver.refresh)
        # cookies_dict = [cookie for cookie in driver.get_cookies()]
        # for item in cookies_dict:
        #     print("Nome: {0} Valor: {1} ".format(item['name'], item['value']))
        # print(driver.get_log)
        # print(driver.get_screenshot_as_file("D:\\Dropbox\\Dropbox\\Meu Curso de Selenium\\
        # testes\\imgs\\videdetestador.png"))
        # print(driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
