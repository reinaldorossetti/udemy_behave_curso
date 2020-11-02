from selenium import webdriver
from time import sleep

# url mostra como criar um profile
# https://support.mozilla.org/pt-BR/kb/gerenciador-de-perfis-para-criar-remover-perfis?redirectlocale=en-US&redirectslug=Managing+profiles

dir = "C:\\GitHub\\udemy_my_course\\browsers\\myprofile"
firefox_profile = webdriver.FirefoxProfile(profile_directory=dir)
driver = webdriver.Firefox(firefox_profile=firefox_profile)

driver.get("http://reinaldorossetti.blogspot.com.br/")

sleep(30) # somente para esperar, e mostrar para os alunos.
