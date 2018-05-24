O Download e a configuração das ferramentas são de suma importância para você seguir no curso, a configuração dos Drivers são necessários pra rodar os testes no browser, sem isso você não vai conseguir seguir em frente.

Ordem de Instalação:

Instalação Local, não usando a maquina virtual:

1. Instalar o Python e adicionar o mesmo no path do windows;

2. Instalar o Selenium WebDriver;

```python
pip install selenium
```

** Se não tiver permissão de administrador (PermissionError), pode ser que der erro, ou não dependendo do seu nível de permissão.

Solução: Abra o CMD/Prompt de comando como administrador.

3. Instalar os drivers (chromedriver, geckodriver, iedriver), você deve adicionar no path do windows ou passar o caminho no código;
Drivers links:

Geckodriver Releases: 

https://github.com/mozilla/geckodriver/releases

IE Driver: 

https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Chrome Driver: 

https://sites.google.com/a/chromium.org/chromedriver/downloads

-----------------------------------------------------------------------------------------------------------

Como mostra a figura, os drivers devem está dentro da pasta Scripts dentro do Python, esse é o caminho padrão, podemos adicionar em qualquer pasta desde que este esteja no path global do windows. Uma vez no path do windows ou adicionada a pasta Scripts não precisa passar o path por dentro do driver, ou seja no código fonte.

> Atenção dependendo do sistema operacional, você tem que baixar o driver especifico pra seu sistema e também para a plataforma x64 ou x86, alguns driver é o mesmo para os dois, mas nem todos. Um erro bem comum é quando você tem o sistema x64 e o driver do geckodriver x64 e a versão do firefox foi instalada pra x86, o que vai gerar vários problemas.

4. Instalar a IDE para desenvolver os testes (Escolha uma entre Atom, Pycharm, Visual Code da Microsoft);

-----------------------------------------------------------------------------------------------------------

### Atenção - Você pode instalar em um ambiente controlado criando um máquina virtual, não é obrigatório, você pode começar na sua máquina mesma. Para instalar em uma VM precisamos instalar o Virtual Box ou VMware Player. Após a instalação da máquina virtual, comece a instalação das ferramentas seguindo os passos acima.

Virtual Box Windows: 

http://download.virtualbox.org/virtualbox/5.1.16/VirtualBox-5.1.16-113841-Win.exe

Virtual Box Linux: 

https://www.virtualbox.org/wiki/Linux_Downloads

Virtual Box MAC:

http://download.virtualbox.org/virtualbox/5.1.16/VirtualBox-5.1.16-113841-OSX.dmg

Download das maquinas virtuais:

https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/


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

** Instalando os Drivers ** - Caso tenha dificuldade em Instalar os Drivers temos uma segunda alternativa no link abaixo:

https://github.com/reinaldorossetti/udemy_my_course/blob/master/ambiente/instalando_driver_via_api.MD

