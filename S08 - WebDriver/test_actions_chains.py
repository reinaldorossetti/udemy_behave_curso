from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
from os import getcwd

# JavaScript: Drag and drop script
# param1 (WebElement): Source element to drag
# param2 (WebElement): Optional - target element for the drop
# param3 (int): Optional - Drop offset x relative to the center of the target or source element
# param4 (int): Optional - Drop offset y relative to the center of the target or source element
# param4 (int): Optional - Delay in milliseconds (default = 1ms) for dragging and dropping

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop2")
driver.implicitly_wait(15)
driver.switch_to.frame("iframeResult")

cwd = getcwd()
JS_DRAG_DROP = open(cwd + '\\drag-drop.js', 'r').read()
print(JS_DRAG_DROP)
# drag and drop an element on another one
source = driver.find_element_by_css_selector("#drag1")
target = driver.find_element_by_css_selector("div#div2")
location1 = int(source.location['x'])

print(driver.execute_script(JS_DRAG_DROP, source, target))
driver.implicitly_wait(5)

source2 = driver.find_element_by_css_selector("#drag1")
print(source2.location)
location2 = int(source2.location['x'])

type(location1)
print(location1, location2)
assert(location2 > location1)


driver.get("http://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop")
driver.implicitly_wait(15)
driver.switch_to.frame("iframeResult")

source = driver.find_element_by_css_selector("img#drag1")
target = driver.find_element_by_css_selector("div#div1")
driver.execute_script(JS_DRAG_DROP, source, target, None, None, 101)


# Not have HTML 5, drag_and_drop_by_offset working very well.
driver.get("http://jsfiddle.net/davidThomas/DGbT3/3/")
driver.implicitly_wait(15)

# drag and drop an element by offset {x:500, y:200}
driver.find_element_by_css_selector("#run").click()
driver.switch_to.frame("result")

source3 = driver.find_element_by_css_selector("#dragThis")
target3 = driver.find_element_by_css_selector("#dropHere")

location1 = int(target3.location['x'])
location2 = int(target3.location['y'])
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(source3, location1+10, location2+10)
actions.perform()

# Not Working
driver.execute_script(JS_DRAG_DROP, source3, None, 500, 200)
print(source3.location)

