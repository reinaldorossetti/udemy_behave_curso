# udemy_my_course
Exemplo usados no meu curso na udemy de python 3 e Selenium.

Na pasta exemplo_selenium_mult_linguagem, vamos comparar as linguagens fazendo um teste simples.

### Vamos primeiro analisar a quantidade de caracteres sem os espaços:
https://github.com/reinaldorossetti/udemy_my_course/blob/master/SELENIUM_MULT_LINGUAGEM_EXEMPLOS.md


# Realizando a instalação do Selenium Webdriver

O Projeto do Official do Selenium suporta as versões do python 2.7 e 3.6.

The latest official release is available on the [Python Package Index](http://python.org/pypi/selenium). It's a good practice to install python packages into [virtual environments](https://packaging.python.org/installing/#creating-and-using-virtual-environments) rather than in your global site packages. 

Para instalar a biblioteca/framework do Selenium utilizamos o comando oficial de instalação dos pacotes pip.
([pip](https://pip.pypa.io/en/stable/installing/)).

 Para realizar a instalação rodamos o comando abaixo no (shell, cmd, prompt do sistema operacional):

```
pip install selenium
```

# Passo a Passo de como usar os comandos:

Para utilizamos as funções do nosso framework, primeiro devemos Importar o módulo, digitando o seguinte comando abaixo no seu shell python/IDE:

```python
from selenium import webdriver
```

Depois de importa a biblioteca devemos instanciar o driver do Selenium, o driver vai fazer a conexão com browser, então o comando é diferente para cada browser, segue os exemplos abaixo de acordo com o browser:

### Firefox

```python
from selenium import webdriver
driver = webdriver.Firefox()
```

### Google Chrome

```python
from selenium import webdriver
driver = webdriver.Chrome()
```

### Internet Explorer

```python
from selenium import webdriver
driver = webdriver.Ie()
```

### Microsoft Edge

```python
from selenium import webdriver
driver = webdriver.Edge()
```

### Safari

```python
from selenium import webdriver
driver = webdriver.Safari()
```


### Remote Driver
Existe uma forma de instanciar o driver utilizando o selenium-server que é um arquivo.jar, nele podemos passar o nome do browser.
```python
from selenium import webdriver
driver = webdriver.Remote(browser_name="firefox", platform="any")
```


# Documentação do Selenium WebDriver

A documentação está disponível online [aqui] (http://seleniumhq.github.io/selenium/docs/api/py/) e pode ser construída localmente usando o comando `tox -e docs`.
## Interactive

Uma alternativamente via shell/prompt usando o console do python para visualizar todos os comandos disponíveis para você, após a importação, executamos o comando abaixo:
```python
dir(webdriver)
```

Para ver as docstrings  (texto da documentação anexado a uma função ou método), execute o comando abaixo:
```python
print(nome_da_funcao_fica_aqui.__doc__)
```
### Exemplo abaixo da função get do Firefox
from selenium import webdriver
print(webdriver.Firefox.get.__doc__)
Resultado:  Loads a web page in the current browser session.


## Comparison with Java Bindings

Here is a summary of the major differences between the python and Java bindings.

### Function Names

Function names separate compound terms with underscores, rather than using Java's camelCase formatting. For example, in python `title` is the equivalent of `getTitle()` in Java.

### Flatter Structures

To reflect pythonic behavior of flat object hierarchies the python bindings e.g. `find_element_by_xpath("//h1")` rather than `findElement(By.xpath("//h1"));` but it does give you the freedom of doing `find_element(by=By.XPATH, value='//h1')`

# Development

To install the latest unreleased version, [clone](https://help.github.com/articles/cloning-a-repository/) https://github.com/SeleniumHQ/selenium and run the following commands from the repository root directory:

```
./go py_prep_for_install_release
cd py
python setup.py install
```

## Tests

When developing Selenium, it is recommended you run the tests before and after making any changes to the code base. To perform these tests, you will first need to install [Tox](http://tox.readthedocs.io/).

> Note that you will either need to change to the `py` subdirectory when running `tox`, or point to the configuration file using `tox -c py/tox.ini`.

By default, running `tox` will attempt to execute all of the defined environments. This means the tests for python 2.7 and 3.6 will run for each of the supported drivers. This is most likely not what you want, as some drivers will not run on certain platforms. It is therefore recommended that you specify the environments you wish to execute. To list all environments available, run `tox -l`, and to execute a single environment, use `tox -e`.

As an example, this command will run the tests for Firefox against python 2.7:

```
tox -e py27-firefox
```

The tests are executed using [pytest](http://docs.pytest.org/), and you can pass positional arguments through Tox by specifying `--` before them. In addition to other things, this allows you to filter tests. For example, to run a single test file:

```
tox -e py27-firefox -- py/test/selenium/webdriver/common/visibility_tests.py
```

To run a single test, you can use the keyword filter, such as:

```
tox -e py27-firefox -- -k testShouldShowElementNotVisibleWithHiddenAttribute
```

### Expected Failures

Unfortunately, there will be some tests that are expected to fail due to known issues. You can mark these tests using the [standard pytest methods](http://docs.pytest.org/en/latest/skipping.html#mark-a-test-function-as-expected-to-fail), however if the test uses the `driver` fixture to run against multiple drivers, this will mark the tests for all of those drivers. If a test is only expected to fail in a subset of drivers, you can extend the xfail mark with the name of the driver. For example, to mark a test as expected to fail in Chrome and Firefox (but pass using any other driver):

```python
import pytest

@pytest.mark.xfail_chrome
@pytest.mark.xfail_firefox
def test_something(driver):
   assert something is True
```

All of the same arguments from pytest's [xfail mark](http://docs.pytest.org/en/latest/skipping.html#mark-a-test-function-as-expected-to-fail) are available to these extended marks. Wherever possible you should provide a `reason` with a reference to the raised issue/bug. If the test raises an unexpected exception you should also provide the `raises` argument, as this will still cause a failure if the test starts failing for another reason.

If the expected failure is dependent on the platform, you should also include the `condition` argument so that the test will be allowed to pass on other environments. For example, to mark a test as expected to fail when run against Firefox on macOS:

```python
import sys
import pytest
from selenium.common.exceptions import WebDriverException

@pytest.mark.xfail_firefox(
    condition=sys.platform == 'darwin',
    reason='https://myissuetracker.com/issue?id=1234',
    raises=WebDriverException
def test_something(driver):
   assert something is True
```

You should avoid using [imperative xfail](http://docs.pytest.org/en/latest/skipping.html#imperative-xfail-from-within-a-test-or-setup-function) as these will never allow the test an opportunity to unexpectedly pass (when the issue is resolved).

We also recommend against using [skip](http://docs.pytest.org/en/latest/skipping.html#marking-a-test-function-to-be-skipped) unless there is good reason. If your test failure causes a hang or some other undesirable side-effect you can pass `run=False` to the xfail mark.

To run expected failures locally, pass the `--runxfail` command line option to pytest. If you want to run all expected failures for a specific driver you can do this by filtering on the xfail mark:

```
tox -e py27-firefox -- -m xfail_firefox --runxfail
```

## Releases

To perform a release you will need to be a maintainer of the package on PyPI. Before pushing a new release you will need to update the version number and [change log](https://github.com/SeleniumHQ/selenium/blob/master/py/CHANGES). The version number is in the form of `X.Y.Z`, where `X.Y` is taken from the latest [GitHub release](https://github.com/SeleniumHQ/selenium/releases), and `Z` increments for each release.

When you're ready, the release can be made by running the following command:

```
./go py_release
```
