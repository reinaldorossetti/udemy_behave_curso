from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://www.google.com")

element = driver.find_element_by_tag_name("input[name='btnI']")

print(element.get_attribute('value'))

driver.quit()
