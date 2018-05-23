** Instalando os Drivers via API ** - Segunda forma de instalar os drivers é usando uma API, ao invés de copiar os mesmos. Vamos lá então!

1. Primeiro Passo instalar o pacote abaixo no prompt/shell:
```
pip install webdriver_manager
```

2. Segundo Passo importar a biblioteca e passar ela dentro do driver (Exemplo usando o Chrome).

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
```

Exemplo usando o Firefox:

```python
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# No caso do firefox se der error acima tente fazer dessa segunda forma.
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.google.com")
```

Exemplo usando o browser Edge:
```python

from selenium import webdriver
from webdriver_manager.driver import EdgeDriver

driver = webdriver.Edge(EdgeDriverManager().install())
driver.get("https://www.google.com")

```
Exemplo usando o browser IE:

```python
from webdriver_manager.driver import IEDriver
from webdriver_manager.microsoft import IEDriverManager

driver = webdriver.Ie(IEDriverManager().install())
driver.get("https://www.google.com")
```

Exemplo usando o browser PhantomJS:
```python
from webdriver_manager.phantomjs import PhantomJsDriverManager
from selenium import webdriver

driver = webdriver.PhantomJS(PhantomJsDriverDriverManager().install())
driver.get("https://www.google.com")
```
Conversando com o caro colega que fez a API, ele disse que caso já esteja instalada ele vai retornar somente o caminho, então não precisa colocar no executable_path depois, pode deixar da forma que estar.

Referências: https://github.com/SergeyPirogov/webdriver_manager
