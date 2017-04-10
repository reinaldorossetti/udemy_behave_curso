from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
# from pymouse import PyMouse

driver = webdriver.Ie()
driver.maximize_window()

driver.get("https://www.gestaojudicial.com.br/Paginas/Principal/_FSet_Abertura.asp")
driver.implicitly_wait(10)

def SelectorWait(driver, locator):
    return WebDriverWait(driver, 45).until(presence_of_element_located((By.CSS_SELECTOR, locator)))


captcha = SelectorWait(driver, "#CodSegCriado")

#CodSegCriado
test = SelectorWait(driver, "#CodSegInformado")
test.send_keys(Keys.ENTER)
print(captcha.get_attribute('value'))
test.send_keys(captcha.get_attribute('value'))


test2 = SelectorWait(driver,"#txtcd_Logon")
# Limpa o campo
test2.clear()
# envia o texto.
test2.send_keys("Udemy")
test2.send_keys(Keys.TAB)

driver.execute_script("""
                var pass = document.getElementById('txtcd_Pwd');
                pass.value = ""
                function Color(){
                var x = document.getElementById('layerTeclado');
                x.style.left = '0px';
                x.style.top = '0px';
                x.style.visibility = 'visible';
                }
                Color();
""")
sleep(2)
driver.execute_script("""
                var list = [ {x:45,y:136},
                             {x:65,y:136},
                             {x:95, y:136} ]
                for (var item in list) {
                        document.elementFromPoint(list[item].x, list[item].y).click();
                }

""")
