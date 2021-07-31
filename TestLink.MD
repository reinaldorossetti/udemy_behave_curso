No TestLink para entrar como administrador no sistema usamos o usuário e password abaixo:
Username: user
Password: bitnami

No servidor:
Username: bitnami
Password: bitnami


Ao Entrar a primeira vez, é recomendado trocar o login e password. 

1. O comando abaixo inicia todos os serviços no servidor:
```
sudo /opt/bitnami/ctlscript.sh start
```
O comando abaixo reinicia somente o serviço do apache server, não precisa usar:
```
sudo /opt/bitnami/ctlscript.sh restart apache
```
O comando abaixo para/stop todos os serviços:
```
sudo /opt/bitnami/ctlscript.sh stop
```
O comando abaixo reinicia todos os serviços:
```
sudo /opt/bitnami/ctlscript.sh restart
```
O comando abaixo lista todos os serviços no servidor:
```
sudo /opt/bitnami/ctlscript.sh  
```

Caso não queira usar uma VM, podemos utilizar um docker:
https://hub.docker.com/r/bitnami/testlink/


Para mais configurações acesso o link abaixo:
https://docs.bitnami.com/virtual-machine/apps/testlink/

Lista de comandos:
https://docs.bitnami.com/general/apps/testlink/administration/control-services/

Página do Testlink:
https://testlink.org

Github do TestLink:
https://github.com/TestLinkOpenSourceTRMS/testlink-code
