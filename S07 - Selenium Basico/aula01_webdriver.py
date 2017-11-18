from selenium import webdriver

"""
Vamos levantar um http server com o comando abaixo:
python -m http.server --bind 127.0.0.1 8083
referencia: http://localhost:8083/html/login.htm
"""

driver = webdriver.Chrome()

driver.get("http://localhost:8083/html/login.html")

elem = driver.find_element_by_id("name123")
elem.send_keys("Reinaldo")

elem02 = driver.find_element_by_class_name("pass123")
elem02.send_keys("12345")

elem03 = driver.find_element_by_css_selector("button[class='form_submit'][type='submit']")
elem03.click()

elem04 = driver.find_element_by_css_selector("div.w3-border")

assert "uname=Reinaldo&psw=12345" in elem04.text

driver.quit()

