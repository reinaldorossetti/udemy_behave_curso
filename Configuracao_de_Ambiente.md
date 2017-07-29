O Download e a configuração das ferramentas são de suma importância para você seguir no curso, a configuração dos Drivers são necessários pra rodar os testes no browser, sem isso você não vai conseguir seguir em frente.

Devemos baixar a versão do driver compatível com o selenium 2.53.6 que estamos usando no curso. No entanto você pode usar versão mais nova do driver com o selenium 3.4.x junto com as versões mais novas de browser (muitas pessoas estão errando ao configurar as versões corretas, entenda que uma versão do driver roda em versão específica de browser,  ou seja não vai rodar em qualquer versão).

Drivers links:

Geckodriver Releases: 

https://github.com/mozilla/geckodriver/releases

IE Driver: 

https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Chrome Driver: 

https://sites.google.com/a/chromium.org/chromedriver/downloads

-----------------------------------------------------------------------------------------------------------

Ordem de Instalação:

Instalação Local, não usando a maquina virtual:

1. Instalar o Python e adicionar o mesmo no path do windows;

2. Instalar o Selenium WebDriver;

>> pip install selenium

** Se não tiver permissão de administrador (PermissionError), pode ser que der erro ou não dependendo do seu nível de permissão.

Solução: Abra o CMD/Prompt de comando como administrador.

3. Instalar os drivers (chromedriver, geckodriver, iedriver), você deve adicionar no path do windows ou passar o caminho no código;

Como mostra a figura, os drivers devem está dentro da pasta Scripts dentro do Python, esse é o caminho padrão, podemos adicionar em qualquer pasta desde que este esteja no path global do windows. Uma vez no path do windows ou adicionada a pasta Scripts não precisa passar o path por dentro do driver, ou seja no código fonte.




>> Atenção dependendo do sistema operacional, você tem que baixar o driver especifico pra seu sistema e também para a plataforma x64 ou x86, alguns driver é o mesmo para os dois, mas nem todos. Um erro bem comum é quando você tem o sistema x64 e o driver do geckodriver x64 e a versão do firefox foi instalada pra x86, o que vai gerar vários problemas.

4. Instalar a IDE para desenvolver os testes (Escolha uma entre Atom, Pycharm, Visual Code da Microsoft);

-----------------------------------------------------------------------------------------------------------

### Atenção - Você pode instalar em um ambiente controlado criando um máquina virtual, não é obrigatório, você pode começar na sua máquina mesma. Para instalar em uma VM precisamos instalar o Virtual Box ou VMware Player. Após a instalação da máquina virtual, comece a instalação seguindo os passos acima.

Virtual Box Windows: 

http://download.virtualbox.org/virtualbox/5.1.16/VirtualBox-5.1.16-113841-Win.exe

Virtual Box Linux: 

https://www.virtualbox.org/wiki/Linux_Downloads

Virtual Box MAC:

http://download.virtualbox.org/virtualbox/5.1.16/VirtualBox-5.1.16-113841-OSX.dmg

Download das maquinas virtuais:

https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/



Python Links:

Windows: https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe

Mac: https://www.python.org/ftp/python/3.5.2/python-3.5.2-macosx10.5.pkg

Linux Shell:

sudo apt-get update
sudo apt-get install python3=3.5.2*


Na dificuldade de instalar o Selenium,  podemos baixar direto do site:

https://pypi.python.org/packages/c9/7f/5741fd1360176c12732e501d697c093d5d2702f3e35b6c3e23ff9c530a57/selenium-3.3.1-py2.py3-none-any.whl#md5=ee834757b54e4cc73fd885d6248dea6e

Após baixa o selenium no link, dentro da pasta abra o cmd e digite o comando abaixo:

pip install selenium-3.3.1-py2.py3-none-any.whl


----------------------------------------------------------------------------------


**APIs que usamos no Curso:**

pip install requests

pip install behave

pip installl selenium

** Pra instalar as APIs, precisamos abrir o cmd ou prompt do Windows e enviar o comando e dar enter, como na foto:



---------------------------------------------------------------------------------



**Behave**

Github: https://github.com/behave/behave

Site: http://pythonhosted.org/behave/

Pacote: https://pypi.python.org/pypi/behave


**Requests**

Github: https://github.com/kennethreitz/requests/

Site:http://docs.python-requests.org/en/master/

Pacote: https://pypi.python.org/pypi/requests/2.13.0



**Selenium**

Github: https://github.com/SeleniumHQ/selenium

Site: http://www.seleniumhq.org/

Pacote: https://pypi.python.org/pypi/selenium



** Links quebrados por favor me avisem, que eu corrijo.

** Tente sempre instalar as ferramentas como administrador.

Nem sempre o windows ou linux vai deixar executar um determinado programa com permissões de administrador mesmo sendo administrador da máquina, isso é uma proteção para melhorar a segurança, é algo padrão do Windows, no caso do Linux você teria que digitar a senha de sudo/administrador da maquina para instalar. No nosso caso precisamos abrir o CMD e IDEs com o modo "Executar como administrador", para evitar erros de ambiente.



** Não esqueça de antes de baixar a ultima versão do selenium, verificar a ultima versão compatível com a versão do driver do browser nos sites especificados.

-----------------------------------------------------------------------------------------------------------

** Instalando os Drivers ** - Segunda forma de instalar os drivers é usando uma API, caso não consiga importar e adicionar ao path do windows, você pode tentar assim:

1. Primeiro Passo instalar o pacote abaixo no prompt/shell:

pip install webdriver_manager
2. Segundo Passo importar a biblioteca e passar ela dentro do driver (Exemplo usando o Chrome).

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")


Exemplo usando o Firefox:

from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
No caso do firefox se der error acima tente fazer dessa segunda forma.

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


Exemplo usando o browser Edge:

driver = webdriver.Edge(EdgeDriverManager().install())
Exemplo usando o browser IE:

driver = webdriver.Ie(IEDriverManager().install())
Exemplo usando o browser PhantomJS:

driver = webdriver.PhantomJS(PhantomJsDriverDriverManager().install())
Conversando com o caro colega que fez a API, ele disse que caso já esteja instalada ele vai retornar somente o caminho, então não precisa colocar no executable_path depois, pode deixar da forma que estar.

Referências: https://github.com/SergeyPirogov/webdriver_manager

