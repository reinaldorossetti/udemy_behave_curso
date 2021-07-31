Para baixar a VM do TestLink acesso o link abaixo:
https://bitnami.com/stack/testlink/virtual-machine

No TestLink para entrar como administrador no sistema usamos o usuário e password abaixo:  
Username: user  
Password: bitnami  

**No servidor:**  
**Username:** bitnami  
**Password:** bitnami  


Ao Entrar a primeira vez, é recomendado trocar o login e password.   

1. O comando abaixo inicia todos os serviços no servidor, o mesmo é um script bash que faz a instalação de todos os serviços: 
```
sudo /opt/bitnami/ctlscript.sh start
```

2. Comando para listar o IP do servidor:  
```
ifconfig
```
Caso der Ifconfig comando not found. Instale a biblioteca abaixo:  
```
apt-get install net-tools
```

Caso der errado use o comando abaixo:  
```
ip address
```


### Os comandos abaixo são opcionais, não necessário para o curso:  
O comando abaixo reinicia somente o serviço do apache server:  
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

Pra quem usar MAC e Linux, talvez seja melhor instalar manual, segue o link abaixo:  
1. No site baixe o binário para seu sistema operacional e faça a instalação do mesmo.  
https://bitnami.com/stack/testlink/installer

Para mais configurações acesso o link abaixo:  
https://docs.bitnami.com/virtual-machine/apps/testlink/  

Lista de comandos:  
https://docs.bitnami.com/general/apps/testlink/administration/control-services/  

Página do Testlink:  
https://testlink.org  

Github do TestLink:  
https://github.com/TestLinkOpenSourceTRMS/testlink-code  
