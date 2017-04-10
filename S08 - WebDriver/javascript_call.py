# importando as bibliotecas necessarias.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

# inicia a instalancia do chrome driver.
driver = webdriver.Chrome()
# aumenta a tela.
driver.maximize_window()
# carrega o site no browser.
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_event_onclick3")
# espera o browser carregar por 10 segundos.
driver.implicitly_wait(10)

# funcao com a espera explicita.
def Wait(driver, locator):
    return WebDriverWait(driver, 60).until(presence_of_element_located((By.CSS_SELECTOR, locator)))

# muda para o frame correto.
driver.switch_to.frame("iframeResult")
# espera a tag h1 se estah presente na tela.
elemento = Wait(driver, "h1")
# faz o assert antes para assegurar que estah na tela correta.
assert "Click on this text!" == elemento.text

# executa nosso javascript.
driver.execute_script("""
test = document.querySelector('h1');
changeText(test);
""")

# faz o assert do elemento apos o onclick.
elemento = Wait(driver, "h1")
assert "Ooops!" == elemento.text
