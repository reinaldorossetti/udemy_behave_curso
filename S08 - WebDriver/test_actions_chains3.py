from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
import win32api
import win32con

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://jsfiddle.net/davidThomas/DGbT3/3/")
driver.implicitly_wait(15)

# Selenium Test with pywin32 library.
# win32api, win32ui, win32con in the same pack.
# Docs: http://docs.activestate.com/activepython/3.2/pywin32/
# Download: https://pypi.python.org/pypi/pypiwin32 or pip install pypiwin32


def move_cursor(x, y):
    # fuction move cursor, below the options.
    # MOUSEEVENTF_LEFTDOWN
    # MOUSEEVENTF_LEFTUP
    # MOUSEEVENTF_RIGHTDOWN
    # MOUSEEVENTF_RIGHTUP
    # MOUSEEVENTF_MIDDLEDOWN
    # MOUSEEVENTF_MIDDLEUP
    # MOUSEEVENTF_ABSOLUTE

    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    sleep(3)


def win_enter():
    win32api.keybd_event(0x0D, 0, 0, 0)
    sleep(.5)
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
    sleep(3)

# Get iframe location x and y.
test = driver.find_element_by_css_selector("#result")
iframe_x = int(test.location['x'])
iframe_y = int(test.location['y'])
print(iframe_x, iframe_y)

driver.find_element_by_css_selector("#run").click()
driver.switch_to.frame("result")

# Get location x and y of elements.
source3 = driver.find_element_by_css_selector("#dragThis")
target3 = driver.find_element_by_css_selector("#dropHere")
elemento_x = int(target3.location['x'])
elemento_y = int(target3.location['y'])


actions = ActionChains(driver)
# Move to web element.
actions.move_to_element(source3)
# Move the cursor via win32 api.
move_cursor(iframe_x + elemento_x, iframe_y + elemento_y)

# Click the right mouse button on the screen.
actions.context_click().perform()
sleep(5)
# Send Enter via windows api.
win_enter()
driver.close()
