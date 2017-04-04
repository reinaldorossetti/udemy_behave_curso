require "selenium-webdriver"

driver = Selenium::WebDriver.for :firefox
driver.navigate.to "http://www.google.com"
element = driver.find_element(:name, 'q')
element.send_keys "Hello Selenium WebDriver!"
element.submit
puts driver.title