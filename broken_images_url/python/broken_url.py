from selenium import webdriver
from selenium.webdriver.common.by import By
from requests import get
# Instanciando o chrome driver.
driver = webdriver.Chrome()

# Abre a url.
driver.get("https://jsfiddle.net/ueztxg19/9/")

# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(10)

# Muda para o frame correto.
driver.switch_to.frame("result")


def test_broken(tag, atributo ):

    # Procura os elementos no browser via CSS Selector.
    elementos = driver.find_elements(By.CSS_SELECTOR, tag)
    print(len(elementos))

    for x in elementos:
        # pega o atributo que eh a url do elemento.
        url = x.get_attribute(atributo)
        # captura o request para comparar o status code.
        request = get(url)
        if request.status_code == 404:
            print("Url Quebrada, url:{} status code:{}".format(url, request.status_code))


test_broken("img", "src")
test_broken("a", "href")
driver.quit()
