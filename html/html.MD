
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

Depois vou detalhar mais coisas...
