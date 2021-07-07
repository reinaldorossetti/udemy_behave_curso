from time import sleep

from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10) # espera implicita de 10 segundos.

driver.get("http://34.117.165.240/")
sleep(10) # load carregar
element = driver.find_elements(By.CSS_SELECTOR,"span[role=slider]")
actions = ActionChains(driver)
actions.move_to_element(element[0]).click_and_hold(element[0]).move_to_element(element[1]).click().perform()

sleep(30)
# pedir pro browser sair.