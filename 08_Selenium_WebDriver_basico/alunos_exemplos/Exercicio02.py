from selenium import webdriver
from selenium.webdriver.common.alert import Alert
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""

driver = webdriver.Chrome()

driver.switch_to.alert.authenticate('cheese', 'secretGouda')

# verifica se realizou o teste com sucesso.
html = driver.page_source
assert "reinaldorossetti.blogspot.com" in html

# pedir pro browser sair.
driver.quit()

