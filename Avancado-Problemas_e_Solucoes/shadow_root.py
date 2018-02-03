import selenium
from selenium import webdriver
#from selenium.webdriver.support.
driver = webdriver.Chrome()


def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

driver.get("chrome://downloads")
root1 = driver.find_element_by_tag_name('downloads-manager')
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element_by_css_selector('downloads-toolbar')
shadow_root2 = expand_shadow_element(root2)

root3 = shadow_root2.find_element_by_css_selector('cr-search-field')
shadow_root3 = expand_shadow_element(root3)

search_button = shadow_root3.find_element_by_css_selector("#search-button")
search_button.click()