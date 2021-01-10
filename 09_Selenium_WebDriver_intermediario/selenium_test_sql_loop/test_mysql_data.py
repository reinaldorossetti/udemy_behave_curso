from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime


class PropertyTest:

    def __init__(self):

        # Instanciando o firefox driver.
        # Passamos o caminho do driver, no meu caso eh linux a barra / eh no windows eh o contrario.
        # Nao esqueca de baixar os drivers e passar o caminho ou deixar no path do windows.
        self.driver = webdriver.Chrome(executable_path="/home/reiload/drivers/chromedriver")
        # Abre a url.
        self.driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_legend")
        # Espera de forma implicita os elementos carregar na pagina.
        self.driver.implicitly_wait(10)
        # Muda para o frame correto.
        self.driver.switch_to.frame("iframeResult")

    def espera_explicita(self, selector, delay=30):
        # Espera Explicita > Melhor forma de fazer.
        # An expectation for checking that an element is present on the DOM of a page and visible.
        return WebDriverWait(self.driver, delay).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def testProperty(self, first_name, last_name):

        self.espera_explicita("input[type='text']")

        # Procura os elementos input na tela via CSS Selector.
        elementos = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

        print(first_name, last_name)
        elementos[0].clear() # Limpa o campo
        elementos[1].clear() # Limpa o campo
        # Envia os valores para os campos.
        elementos[0].send_keys(first_name)
        elementos[1].send_keys(last_name)

        submit = self.driver.find_element(By.CSS_SELECTOR, "input[type*='submit']")
        submit.click()
        # pega o elemento pra confirmar o cadastro ou seja para fazer assert final.
        variavel_texto = self.espera_explicita("div.w3-large.w3-border")

        # Fazendo o assert
        assert "firstname={}&lastname={}".format(first_name,last_name) == \
                variavel_texto.text
        # fecha o browser
        self.driver.close()
