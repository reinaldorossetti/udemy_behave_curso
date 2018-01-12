from selenium import webdriver
from selenium.webdriver.common.by import By
"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""

driver = webdriver.Chrome()

driver.get("http://localhost:8083/html/login.html")
# em caso de falha por não localizar o elemente, descomente a linha abaixo.
# driver.implicitly_wait(30)

driver.find_element(By.ID, "name123").send_keys("Reinaldo")

driver.find_element(By.ID, "pass123").send_keys("12345")

driver.find_element(By.CSS_SELECTOR, "button[class='form_submit'][type='submit']").click()

elem = driver.find_element(By.CSS_SELECTOR, "div.w3-border")

assert "uname=Reinaldo&psw=12345" in elem.text

driver.quit()

