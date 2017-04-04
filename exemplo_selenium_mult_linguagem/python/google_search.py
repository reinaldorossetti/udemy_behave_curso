from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.google.com")
element = driver.find_element_by_name("q")
element.send_keys("Hello WebDriver!")
element.submit()
print(driver.title)