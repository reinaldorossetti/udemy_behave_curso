

### Primeiro vamos instalar a biblioteca que vai gerar o report com o behave.
``` shell
pip install allure-behave
```

### Executando o comando que vai pegar o report do behave e fazer o parse para o allure.
``` shell
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
```

### Agora vamos subir os nossos reports no allure server.
```shell
allure serve %allure_result_folder%
```
