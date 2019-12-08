## 1.1. Introdução

O Selenium é um projeto abrangente que engloba uma variedade de ferramentas e bibliotecas, permitindo a automação do navegador para web. O Selenium fornece especificamente infraestrutura para a especificação W3C WebDriver - uma plataforma e uma interface de codificação de idioma neutro compatível com todos os principais navegadores da web.

[W3C WebDriver](https://www.w3.org/TR/webdriver1/)

O Selenium Python fornecem uma API simples para escrever testes funcionais e de aceitação usando o Selenium WebDriver. Através da Biblioteca Selenium Python, você pode acessar todas as funcionalidades do Selenium WebDriver de maneira intuitiva.

A biblioteca Cliente do Selenium fornece uma API conveniente para acessar o Selenium WebDrivers como Firefox, Ie, Chrome, Remote etc. As versões atuais suportadas do Python são 2.7, 3.5 e superior. Todos os comandos no final das contas vai para o Driver do Browser, o mesmo que executa os comandos no browser, cada browser fornece seu driver.


### 1.2 Instalação do Python

Nosso primeiro passo é instalar o Python de acordo com o seu Sistema Operacional, seja ele Windows, Linux e MacOS. No curso temos os vídeos de instalação, menos no caso do MacOS, mas temos os comando via Terminal ou o executável do mesmo.


#### Passo a Passo para Instalação do Python no Windows, no link abaixo:

https://github.com/reinaldorossetti/udemy_my_course/blob/master/Instalando_o_python.MD


Instalação no Linux via Terminal
```
sudo apt-get update sudo apt-get install python3=3.5.4*
```

Instalação no MacOS via Terminal:
```
brew install python
```

Link do Python para Mac instalação via executável, os passos é semelhante ao windows:
https://www.python.org/ftp/python/3.5.4/python-3.5.4-macosx10.6.pkg


### Fazendo Download do Selenium:

É possível fazer o download da Biblioteca do Selenium na página PyPI para pacote [selenium](https://pypi.python.org/pypi/selenium). Contudo, uma abordagem melhor seria usar [pip](https://pip.pypa.io/en/latest/installing) para instale o pacote selenium. O Python 3.6 possui pip disponível na biblioteca padrão, [Python](https://docs.python.org/3.6/installing/index.html).

Usando o **pip** , você pode instalar o selenium no console/terminal (CMD) assim:
```
  pip install selenium
```
** Em alguns casos em que temos selenium 2 e 3 instalado vai usar o "pip3 install selenium" sem aspas duplas pra executar o comando.  
** Se não tiver permissão de administrador (PermissionError), pode ser que der erro, depende do seu nível de permissão.  

Você pode considerar o uso de [virtualenv](http://www.virtualenv.org>), para criar ambientes Python isolados. Python 3.6 tem [pyvenv](https://docs.python.org/3.6/using/scripts.html#scripts-pyvenv), que é quase o mesmo que virtualenv.







