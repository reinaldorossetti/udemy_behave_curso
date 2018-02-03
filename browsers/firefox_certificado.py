from selenium import webdriver
from time import sleep


# configurando o firefox para aceitar o certificados não confiaveis.

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("webdriver_accept_untrusted_certs", value=True)
firefox_profile.set_preference("webdriver_assume_untrusted_issuer", value=True)
driver = webdriver.Firefox(firefox_profile=firefox_profile)

# um certificado revogado.
driver.get("https://revoked.grc.com/")

sleep(5) # somente para esperar, e mostrar para os alunos.

# um certificado expirado.
driver.get("https://wrong.host.badssl.com/")

sleep(5) # somente para esperar, e mostrar para os alunos.