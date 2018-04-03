
Aula sobre HTML Básico.

Link Usado:
https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_button_formmethod

Código da Aula:
https://github.com/reinaldorossetti/udemy_my_course/blob/master/html/html-estrutura.html

```HTML
<!DOCTYPE html>
<html>
    <head>
        <title>Primeiro Exemplo.</title>
        <style>
            body {background-color: powderblue;}
            h1   {color: blue;}
            p    {color: red;
                    font: 16px Arial;}
        </style>
    </head>

    <body>
        <div id="text123">
            <p>Meu texto fica aqui</p>
        </div>
        <form action="https://www.w3schools.com/action_page.php?" method="get">
          First name: <input type="text" name="fname" value="Reinaldo"><br>
          Last name: <input type="text" name="lname" value="Mateus"><br>
          <input type="submit" value="Submit">
          <input type="submit" formmethod="post" formaction="/action_page_post.php" value="Submit using POST">
        </form>
        <script type="text/javascript">
            alert(document.querySelector('form input[value="Submit"]').click())
        </script>
    </body>
</html>
```

1. A declaração <! DOCTYPE html> não é uma tag HTML. É uma instrução para o navegador web sobre a versão do HTML em que a página está escrita.

2. Inicia com a tag <html> e fecha nosso código da página com a tag </html>, o Barra (caractere)  dentro de uma tag significa que você está fechando ela.

3. O conteúdo da página HTML é dividido entre o head e o body, O Head geralmente falamos que o cabeçalho da página contém o título da página, folhas de estilos (formatação via css), entre outras informações sobre a página.
O Body contém todo conteúdo texto e multimidia da página, também o javascript ou jquery que são adicionados ao conteúdo.
<br/>

### **Elementos Web Usados nesse exemplo:**

**title** - Define um título para o documento.  
**style** - Define informações de estilo para um documento.  
**div** - Define uma seção no documento, podemos dizer que define um bloco de elementos html. Geralmente muito usados para separar os componentes HTML que vemos na Página.  
**p** - Define um parágrafo, ou seja um bloco de texto.  
**form** - Define um formulário HTML para entrada de dados para o usuário. Nele podemos fazer via método GET ou POST.  
**input** - Define um controle de entrada.  
**script** - Define um script do lado do cliente.  

<br/>
Nesse exemplo fizemos uma requisição local, via o nosso http server local, para isso enviamos o comando abaixo, devemos fazer primeiro a instalação do python para reproduzir o exemplo, não se incomode que iremos fazer isso nas próximas aulas.<br/>

1. Criar o servidor local: <br/>
![http server](https://github.com/reinaldorossetti/udemy_my_course/blob/master/imagens/serverPython.png)
> Criamos um folder via mkdir udemy_curso e depois entramos nele via cd udemy_curso. 
> Depois digitamos o comando: ***python -m http.server --bind 127.0.0.1 8083***

2. Copiar o código acima para dentro de um arquivo texto e salvar como .html, dentro da pasta do nosso servidor local.  
3. No código fonte acima fizemos um alert ou seja popup que vai disparar o nosso clique no elemento, tudo isso via javascript. 
> somente devemos entrar no browser, e copiar a url no browser: http://localhost:8083/
<br/>
>> Para localizar o elemento usamos a DOM, o comando document.querySelector("CSS Selector do Elemento") em seguida o comando .click()
https://www.w3schools.com/jsref/dom_obj_document.asp
<br/>
4. Após dispara o elemento ele vai realizar um GET no servidor, ou seja envia os dados para o Servidor.  

Instalando o Python, siga o exemplo abaixo:
https://github.com/reinaldorossetti/udemy_my_course/blob/master/Instalando_o_python.MD
