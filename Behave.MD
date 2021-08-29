###O que é Behave?
Behave é uma biblioteca\framework de testes mais popularar em python, o mesmo se baseia no uso da linguagem **Gherkin**.
Sua função é padronizar a forma de descrever especificações de cenários, baseado na regra de negócio.

O BDD se concentra em obter uma compreensão clara do comportamento de software desejado por meio da discussão com as partes interessadas. 
Ele estende que devemos escrever casos de teste em uma linguagem natural que os não-programadores podem ler. 
Isso permite que os desenvolvedores se concentrem em por que o código deve ser criado, ao invés dos detalhes técnicos, 
e minimiza a tradução entre a linguagem técnica em que o código é escrito e a linguagem de domínio falada pela empresa, usuários, 
partes interessadas, gerenciamento de projetos, etc. .
**BDD é o processo como todo, não deve ser usada somente na automação, mas sim quando o time usa essa técnica. Na automação somente é uma consequência do processo como todo.**
**O Behave somente faz a execução dos testes e documentação do mesmo, não interage com o browser, para isso tem o Selenium **

Vamos ver como funciona o Behave:
Os arquivos de recursos são escritos por seu analista de negócios\stakeholders quem quer que tenha seus cenários de comportamento. 

Essas etapas do cenário são mapeadas com implementações de etapas escritas em Python.

E, opcionalmente, existem alguns controles ambientais (código para executar antes e depois das etapas, cenários, recursos ou toda a partida de tiro).

Antes disso, é preciso entender que no Gherkin existem “keywords” (ou “palavras-chave”) a serem utilizadas para especificar a forma como cada step interage com o sistema. 
Dentre todas, as essenciais são:

Given (pt: Dado): Utilizado para especificar uma pré condição, dentro desse step é feita a validação de uma condição antes de se prosseguir para os próximos passos. 
Por se tratar de uma pré condição, normalmente vem escrito no passado;

When (pt: Quando): Utilizado quando será executada uma ação de que se espera uma reação vinda do sistema, que será validada no step “Then”. Este passo geralmente escrito no presente;

Then (pt: Então): Valida se o esperado aconteceu. Segue sempre um passo do tipo “Quando”, pois aqui é validada a reação da ação recebida. Por se tratar do resultado esperado, normalmente vem escrito na forma de futuro próximo;

And (pt: E): Caso seja necessário mais uma interação com o sistema para complementar um fluxo, mas que não necessariamente se trata de uma ação ou reação, se utiliza “And”;

But (pt: Mas): No geral serve a mesma funcionalidade do “And”, porém é normalmente utilizado após uma validação negativa depois do “Then”;


Environmental Controls (environment.py) In Python Behave.
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

Exemplo:
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

O Behave Framework foi escrito por Jens Engel, Benno Rice e Richard Jones.


Para mais detalhes acesso o link abaixo:  
https://behave.readthedocs.io/en/stable/
https://github.com/behave/behave

Documentação em PDF:
https://buildmedia.readthedocs.org/media/pdf/behave/latest/behave.pdf