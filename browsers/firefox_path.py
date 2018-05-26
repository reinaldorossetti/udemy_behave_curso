from selenium import webdriver
from time import sleep

dir_ff = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
drivers = r"C:\drivers\geckodriver.exe"

driver = webdriver.Firefox(firefox_binary=dir_ff, executable_path=drivers)
driver.get("http://reinaldorossetti.blogspot.com.br/")

sleep(30) # somente para esperar, e mostrar para os alunos.