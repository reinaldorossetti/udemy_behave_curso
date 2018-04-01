
Aula sobre HTML Básico.

Link Usado:
https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_button_formmethod

Código da Aula:
https://github.com/reinaldorossetti/udemy_my_course/blob/master/html/html-estrutura.html

```HTML
<!DOCTYPE html>
<html>
    <head>
        <title></title>
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

3. O conteúdo da página HTML é dividido entre o head e o body, O Head geralmente falamos que o cabeçalho da página contém o titulo da página, folhas de estilos (formatação via css), entre outras informações sobre a página.
O Body contém todo conteúdo texto e multimidia da página, também o javascript ou jquery que são adicionados ao conteúdo.


Depois vou detalhar mais coisas...
