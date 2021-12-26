from time import sleep
from pathlib import Path
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10) # espera implicita de 10 segundos.

# MUDE O CAMINHO PARA O SEU, EXEMPLO COM MEU USUARIO.
user_data_dir = Path('C:\\Users\\reina\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options = webdriver.ChromeOptions()

# ADICIONA O CAMINHO DO PROFILE
options.add_argument("--user-data-dir={}".format(user_data_dir))

# USE THIS IF YOU NEED TO HAVE MULTIPLE PROFILES
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)

driver.get("https://google.com/")

sleep(15) # somente pra ver

driver.quit()
# pedir pro browser sair.
