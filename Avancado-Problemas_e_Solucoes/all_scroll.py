from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from os import path

ROOT_DIR = path.dirname(path.abspath(__file__))

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://github.com/reinaldorossetti/capybara_tips")
# driver.implicitly_wait(10)
# element = driver.find_element_by_id("day")
# elem = Select(element).select_by_visible_text("3")
sleep(5)
altura = driver.execute_script("return document.documentElement.scrollHeight")
largura = driver.execute_script("return document.documentElement.scrollWidth")
print(altura, largura)
driver.set_window_size(int(largura), int(altura))
sleep(5)
driver.save_screenshot(ROOT_DIR + "/test_print_body2.png")

element = driver.get_screenshot_as_png()

with open(ROOT_DIR + "/test_print_body.png", "wb") as file:
    file.write(element)

sleep(10)

driver.close()