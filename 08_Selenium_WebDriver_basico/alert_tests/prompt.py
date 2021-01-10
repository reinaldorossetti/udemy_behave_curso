from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
"""

driver = webdriver.Chrome()
driver.maximize_window

# windows path
driver.get("http://127.0.0.1:8083/html/prompt.html")

# linux path
# driver.get("http://127.0.0.1:8083/alert_tests/html/prompt.html")
driver.implicitly_wait(10)

test = driver.find_element("id","prompt")
test.click()
sleep(5)
alert = Alert(driver)
print(alert.text)
sleep(3)
nome = "Reinaldo Mateus"
alert.send_keys(nome)
alert.accept()

test2 = driver.find_element("id","demo")
assert test2.text == nome

sleep(10)
driver.quit()