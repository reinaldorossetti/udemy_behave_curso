### 1. O que é o Behave?  

Behave é uma biblioteca\framework de testes mais popularar em python, o mesmo se baseia no uso da linguagem **Gherkin**.  
Sua função é padronizar a forma de descrever especificações de cenários, baseado na regra de negócio.  
**O Behave somente faz a execução dos testes e a documentação do mesmo, não interage com o browser, para isso tem o Selenium.**  

### 2. Antes de Falar mais sobre Behave precisamos entender o BDD.

   O BDD se concentra em obter uma compreensão clara do comportamento de software desejado por meio da discussão com as partes interessadas.   
   No BDD devemos escrever casos de teste em uma linguagem natural, que os não-programadores possam ler e compreender.   
   Isso permite que os desenvolvedores se concentrem em por que o código deve ser criado, ao invés dos detalhes técnicos,   
   e minimiza a tradução entre a linguagem técnica em que o código é escrito e a linguagem de domínio falada pela empresa, usuários,   
   partes interessadas, gerenciamento de projetos, etc. .  
   **BDD é o processo como todo, não deve ser usada somente na automação, mas sim quando o time usa essa técnica. Na automação somente é uma consequência do processo como todo.**  

   O principio básico do Behave diz que devemos escrever as features ou histórias de usuário, pelos analistas de negócios e os stakeholders quem quer que tenha dominio dos cenários de negócio.   
   As etapas dos cenários são mapeadas com implementações de etapas escritas em Python com o Behave framework, após a escrita das features.  

### 3. Keywords  
   Antes disso, é preciso entender que no Gherkin existem os “keywords” (ou “palavras-chave”) a serem utilizadas para especificar a forma como cada step interage com o sistema.   
   Dentre todas, as essenciais são:  

   **Given** (pt: Dado): Utilizado para especificar uma pré condição, dentro desse step é feita a validação de uma condição antes de se prosseguir para os próximos passos.   
   Por se tratar de uma pré condição, normalmente vem escrito no passado. 

   **When** (pt: Quando): Utilizado quando será executada uma ação de que se espera uma reação vinda do sistema, que será validada no step “Then”.   
   Este passo geralmente escrito no presente;  

   **Then** (pt: Então): Valida se o esperado aconteceu. Segue sempre um passo do tipo “Quando”, pois aqui é validada a reação da ação recebida.   
   Por se tratar do resultado esperado, normalmente vem escrito na forma de futuro próximo.  

   **And** (pt: E): Caso seja necessário mais uma interação com o sistema para complementar um fluxo, mas que não necessariamente se trata de uma ação ou reação, se utiliza “And”.  
   **But** (pt: Mas): No geral serve a mesma funcionalidade do “And”, porém é normalmente utilizado após uma validação negativa depois do “Then”.  

### 4. Environmental Controls (environment.py) In Python Behave.  
   Environment.py é um arquivo de ambiente que contém os famosos "Hooks" do Behave.   
   É ser usado para definir o código que deve ser executado antes e depois da ocorrência de certos eventos,  
    durante o ciclo de automação do teste com o Selenium.  

   Alguns das funções comuns que podem ser usados que chamamos de Hooks no Behave, segue estão abaixo:  

   before_step(context, step) - Palavra chave para executar comandos antes de cada step.  
   after_step(context, step) – Palavra chave para executar comandos depois de cada step.  
   before_scenario(context, scenario) - Palavra chave para executar antes de cada cenário.  
   after_scenario(context, scenario) – Palavra chave para executar depois de cada cenário.  
   before_all(context) - Palavra chave para executar algo antes de todo o ciclo de teste. Geralmente executar um comando global para suite inteira de testes. Exemplo Maximizar a tela.  
   after_all(context) – Palavra chave para executar algo antes de todo o ciclo de teste. Geralmente executar um comando global para suite inteira de testes.   

### 5 Exemplos:
1. PT
```feature
Funcionalidade: Barra de busca

Cenário: Busca por repositório no GitHub
    Dado que entrei no site do "GitHub"
    Quando digitar "udemy behave curso" na barra de busca
        E clicar em "All GitHub"
    Então o repositório será encontrado
``` 

2. EN
```feature
Scenario Outline: Blenders
   Given I put <thing> in a blender,
    when I switch the blender on
    then it should transform into <other thing>

 Examples: Amphibians
   | thing         | other thing |
   | Red Tree Frog | mush        |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |
```

O Behave Framework foi escrito por Jens Engel, Benno Rice e Richard Jones, versão 1.0 foi feita em 2011.

### 6. Estrutura básica de um projeto com o Behave.  
1. Pasta features é a pasta root do behave:   
features/  

2. Arquivos .feature, é aonde escrevemos o **Gherkin** (features com os cenários):  
features/signup.feature  
features/login.feature  
features/account_details.feature  

3. Arquivo de Ambiente:  
features/environment.py  

4. Pasta "steps" de implementação dos passos:  
features/steps/  
features/steps/website.py  
features/steps/utils.py  


Para mais detalhes acesse os links abaixo:    
https://behave.readthedocs.io/en/stable/  
https://github.com/behave/behave  
https://pypi.org/project/behave    

Documentação em PDF:  
https://buildmedia.readthedocs.org/media/pdf/behave/latest/behave.pdf  
