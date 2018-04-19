from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.implicitly_wait(10) # espera implicita de 10 segundos.

driver.get("https://www.google.com.br")

# como vc tem id no elemento, sempre dar prioridade por id que eh mais rápido e seguro.
element = driver.find_element_by_id("lst-ib")

# faz a ação
element.send_keys("Blog vida de testador")

# faz a busca novamente após a ação.
element = driver.find_element_by_id("lst-ib")

# somente pra saber se enviou.
print(element.get_attribute('value'))

# Exemplo dando o clique via teclado no mesmo elemento, no google fazendo isso jah faz a pesquisa.
# element.send_keys(Keys.ENTER)

# dessa forma voce faz direto via o nome do elemento, sem precisar colocar o input[name=btnK].
element02 = driver.find_element_by_name("btnK")

color = element02.value_of_css_property("color")

print(color)

# verifica se realizou o teste com sucesso.
assert "rgba(117, 117, 117, 1)" in color

# pedir pro browser sair.
driver.quit()

