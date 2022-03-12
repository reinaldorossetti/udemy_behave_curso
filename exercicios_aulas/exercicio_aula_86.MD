
Para resolver o exercicio com Actions Chains, vai precisar ajustar o offset, 
o Selenium quando não idenfica corretamente a posição e vai dar click no meio da tela, assim abrindo o sol. 
Para resolver o problema, peguei as coordenadas no próprio elemento, e adicionei no comando.

Elemento Web:
```
<area shape="circle" coords="124,58,8" 
onmouseover="writeText('Until the 1960s, Venus was often considered a twin sister to the Earth because Venus is the nearest planet to us, and because the two planets seem to share many characteristics.')" 
href="venus.htm" target="_blank" alt="Venus">
```
Adicionando as coords no comando do Selenium:
```
move_to_element_with_offset(element2, 124, 58)
```

Código completo:
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_imagemap")

driver.switch_to.frame("iframeResult")
element2 = driver.find_element(By.CSS_SELECTOR, "map").find_element(By.CSS_SELECTOR, "area[href^=\"venus.htm\"]")
ac = ActionChains(driver)
ac.move_to_element_with_offset(element2, 124, 58)
ac.click().perform()

```

Lista de Comandos pode encontrar no site abaixo:

https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

Exercicio Resolvido:
https://github.com/reinaldorossetti/udemy_behave_curso/blob/professor/09_Selenium_WebDriver_intermediario/ActionChains/exercicio_aula_86.py
