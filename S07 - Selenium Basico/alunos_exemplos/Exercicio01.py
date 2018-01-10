from selenium import webdriver
from selenium.webdriver.common.keys import Keys
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""

driver = webdriver.Chrome()

driver.get("http://www.google.com.br")
# como vc tem id no elemento, sempre dar prioridade por id que eh mais rápido e seguro.
element = driver.find_element_by_id("lst-ib")
# faz a ação
element.send_keys("Blog vida de testador")

# faz a busca novamente após a ação.
element = driver.find_element_by_id("lst-ib")

# somente pra saber se enviou.
print(element.get_attribute('value'))

# dar o clique via teclado no mesmo elemento, no google fazendo isso jah faz a pesquisa.
element.send_keys(Keys.ENTER)
driver.save_screenshot("teste_com_sucesso_imagem.png")

# validar se realizou o teste com sucesso.
html = driver.page_source
assert "reinaldorossetti.blogspot.com" in html

# pedir pro browser sair.
driver.quit()

