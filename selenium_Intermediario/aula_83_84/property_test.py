from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


class PropertyTest:

    def test(self, driver):
        # muda para o frame correto.
        driver.switch_to.frame(0)

        # Procura o elemento na tela via CSS Selector.
        elemento = driver.find_element(By.CSS_SELECTOR, "h3")

        print(elemento.text)

        # Armazenar o elemento texto da tag a
        variavel_texto = elemento.text

        # Armazenar o atributo href da tag a
        variavel_url = str(elemento.get_property("baseURI"))

        # imprimindo no console os valores texto e url.
        print(variavel_url)

        # Fazendo os assert, se os valores sao diferentes do esperado o assert vai falhar ou
        # seja nosso teste falhou.
        assert "Frame A" == variavel_texto
        assert "http://localhost:9090/html/frame_a.htm" == variavel_url


start = datetime.now()
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.set_page_load_timeout(15)
driver.get("http://localhost:9090/html/frameset.html")
test = PropertyTest()
test.test(driver)
driver.quit()
print(datetime.now() - start)