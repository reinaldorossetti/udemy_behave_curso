# Precisa instalar a Biblioteca primeiro, copiar para o console do sistema o comando abaixo.
# Depois somente dar enter no comando abaixo, sem o #.
# pip install webdriver_manager

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# No caso do firefox se der error acima tente fazer dessa segunda forma.
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
