from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# Usando o profile e alterando em tempo de execução o caminho do download

dir = "C:\\Users\\reina\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\laucicqm.reiload"
firefox_profile = webdriver.FirefoxProfile(profile_directory=dir)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.implicitly_wait(30)
driver.get("about:config")
driver.find_element_by_id("warningButton").click()
driver.find_element_by_id("about-config-search").send_keys("browser.download.dir")
driver.find_element_by_css_selector("button[class=button-edit]").click()
driver.find_element_by_css_selector("#form-edit input[type=text]").send_keys("C:\\Users\\reina\\OneDrive\\Aulas")
driver.find_element_by_css_selector("#form-edit input[type=text]").send_keys(Keys.RETURN)
driver.get("http://www.orimi.com/pdf-test.pdf")

sleep(30) # somente para esperar, e mostrar para os alunos.