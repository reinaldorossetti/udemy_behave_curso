from selenium import webdriver
from time import sleep

# url mostra como criar um profile
# https://support.mozilla.org/pt-BR/kb/gerenciador-de-perfis-para-criar-remover-perfis?redirectlocale=en-US&redirectslug=Managing+profiles

dir = "C:\\Users\\reina\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\laucicqm.reiload"
firefox_profile = webdriver.FirefoxProfile(profile_directory=dir)
driver = webdriver.Firefox(firefox_profile=firefox_profile)


driver.get("http://www.orimi.com/pdf-test.pdf")

sleep(30) # somente para esperar, e mostrar para os alunos.
