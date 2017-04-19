# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class Facebook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.facebook.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_facebook(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("pass").clear()
        driver.find_element_by_id("email").send_keys("teste")
        driver.find_element_by_id("pass").clear()
        driver.find_element_by_id("pass").send_keys("teste")
        driver.find_element_by_css_selector("#loginbutton input[type='submit']").click()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
