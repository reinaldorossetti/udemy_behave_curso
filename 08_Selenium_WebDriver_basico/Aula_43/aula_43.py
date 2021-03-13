from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://automacaocombatista.herokuapp.com/users/new")
driver.fullscreen_window()

driver.set_page_load_timeout(10)
driver.find_element_by_id("user_name")
driver.find_element_by_class_name("new_user")
driver.find_element_by_css_selector("#user_lastname")
driver.find_element_by_xpath("//*[@id=\"user_lastname\"]")
driver.find_element_by_name("user[email]")
driver.find_element_by_link_text("Treinamento")
driver.find_element_by_partial_link_text("Busca de")
print(driver.current_url)
#print(driver.page_source)
print(driver.title)
driver.quit()