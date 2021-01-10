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
driver.get("http://127.0.0.1:8083/html/alert.html")
# linux path
# driver.get("http://127.0.0.1:8083/alert_tests/html/alert.html")

driver.implicitly_wait(10)

test = driver.find_element("id", "alert")
test.click()
sleep(5)
alert = Alert(driver)
alert.dismiss()

driver.get("http://127.0.0.1:8083/html/confirm.html")
driver.implicitly_wait(10)

test = driver.find_element("id", "confirm")
test.click()
sleep(5)
alert = Alert(driver)
alert.dismiss()
test = driver.execute_script("return test")
print(test)

driver.quit()