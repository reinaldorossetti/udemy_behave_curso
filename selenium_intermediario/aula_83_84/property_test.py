from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


"""
Vamos levantar um http server local.
1. No terminal\prompt de comando, entre na pasta "selenium_intermediario"
2. Envie o comando abaixo no terminal do seu SO ou no Terminal da IDE.
python -m http.server --bind 127.0.0.1 9090
ou execute o arquivo: http_server.py
3. Abra a url: http://localhost:9090/html/frameset.html
4. Somente executar o script agora.
versões usadas:
    Selenium: 3.141.0
    Python: 3.9
"""


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

        # Fazendo os assert, se os valores sao diferentes do esperado o assert vai falhar ou seja nosso teste falhou.
        assert "Frame A" == variavel_texto
        assert "http://localhost:9090/html/frame_a.htm" == variavel_url


# pega a data atual
start = datetime.now().replace(microsecond=0)
# instancia o browser e configura
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.set_page_load_timeout(15)
driver.get("http://localhost:9090/html/frameset.html")

# instancia a nossa classe e chama a funcao que vai executar o teste.
test = PropertyTest()
test.test(driver)
# fecha a instancia e o browser.
driver.quit()

# mostra a duracao do nosso teste.
time = (datetime.now().replace(microsecond=0) - start)
print("Tempo:{}".format(time))
