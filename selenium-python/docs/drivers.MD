O Selenium requer um driver para interagir com o navegador escolhido. O Firefox, por exemplo, requer o geckodriver, 
que precisa ser instalado antes de executar os scripts de automação.
Cada driver tem sua prória configuração que chamamos de capabilities, os capabilities vai determinar as configurações que vão rodar no meu navegador, se eu não setar um profile ele vai usar as configurações padrão, por padrão ele roda limpo de qualquer configuração local.

[capabilities](https://selenium.dev/documentation/en/driver_idiosyncrasies/driver_specific_capabilities/)

O não cumprimento desta etapa causará um erro:
```
 selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
```

Outros navegadores suportados terão seus próprios drivers disponíveis. Links para alguns dos drivers de navegador mais populares a seguir.

**Temos que baixar o driver nos sites abaixo e copiar para dentro da pasta do python em scripts.**

+--------------+----------------------------------------------------------------------+  
| **Chrome**:  | https://sites.google.com/a/chromium.org/chromedriver/downloads       |  
+--------------+----------------------------------------------------------------------+  
| **Edge**:    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |  
+--------------+----------------------------------------------------------------------+  
| **Firefox**: | https://github.com/mozilla/geckodriver/releases                      |  
+--------------+----------------------------------------------------------------------+  
| **Safari**:  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/         |  
+--------------+----------------------------------------------------------------------+  
| **IE**:      | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |  
+--------------+----------------------------------------------------------------------+  

** Instalando os Drivers ** - Caso tenha dificuldade em Instalar os Drivers temos uma segunda alternativa no link abaixo:  

https://github.com/reinaldorossetti/udemy_my_course/blob/master/ambiente/instalando_driver_via_api.MD  

** Se não tiver permissão de administrador (PermissionError), pode ser que der erro, ou não dependendo do seu nível de permissão.
-> Solução: Abra o CMD/Prompt de comando como administrador.  

https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/  

No linux precisamos dar permissão no driver:  
```
chmod -R 777 geckodriver  
```

Siga as instruções abaixo em caso de problema:  

https://selenium.dev/documentation/en/webdriver/driver_requirements/  
