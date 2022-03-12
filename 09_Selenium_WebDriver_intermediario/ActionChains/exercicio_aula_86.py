from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_imagemap")

driver.switch_to.frame("iframeResult")
element2 = driver.find_element(By.CSS_SELECTOR, "map").find_element(By.CSS_SELECTOR, "area[href^=\"venus.htm\"]")
ac = ActionChains(driver)
ac.move_to_element_with_offset(element2, 124, 58)
ac.click().perform()
