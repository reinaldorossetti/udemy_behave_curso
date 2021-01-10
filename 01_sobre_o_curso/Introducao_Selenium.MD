## Introdução ao Selenium WebDriver
O Selenium oferece suporte à automação de todos os principais navegadores do mercado através do uso de WebDriver.   
O WebDriver é uma API e protocolo que define uma interface com uma linguagem comum para controlar o comportamento dos navegadores da web.   
Cada navegador é tem sua implementação do WebDriver específica, chamada de driver. O driver é o componente responsável por delegar ao navegador e controla a comunicação entre o Selenium e o navegador.  

Essa separação é parte de um esforço consciente para que os fornecedores de navegadores assumam a responsabilidade pela implementação dos drivers para fazer a comunicação. A Selenium faz uso desses drivers de terceiros sempre que possível, mas também fornece seus próprios drivers mantidos pelo projeto para os casos em que isso não seja uma realidade.  

A estrutura do Selenium une todas essas peças por meio de uma interface voltada para o usuário que permite que os diferentes back-ends do navegador sejam usado de forma transparente, permitindo a automação entre navegadores e plataformas\linguagens diferentes.  

Mais detalhes:   
https://www.selenium.dev/documentation/en/introduction/the_selenium_project_and_tools/  
https://www.selenium.dev/documentation/en/webdriver/driver_requirements/