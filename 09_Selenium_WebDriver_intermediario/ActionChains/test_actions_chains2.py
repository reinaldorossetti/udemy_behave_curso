from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import os
from json import loads
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/drag_and_drop")
driver.implicitly_wait(15)
driver.switch_to.frame("iframeResult")

elem_from = "img#drag1"
elem_to = "div#div1"

cwd = os.getcwd()
fo = open(cwd + "\\drag_and_drop_helper.js", "r")
dnd_javascript = fo.read()

print(str(dnd_javascript)+"$('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
test = driver.execute_script(str(dnd_javascript)+"$('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
print(test)
