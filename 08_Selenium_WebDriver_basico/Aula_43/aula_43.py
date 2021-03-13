from selenium import webdriver

# instancia e carrega a nossa pagina.
driver = webdriver.Chrome()
driver.get("https://automacaocombatista.herokuapp.com/users/new")

# funcao para deixar a tela cheia.
driver.fullscreen_window()

# tempo maximo para ler os elementos da pagina, isso na leitura\abertura da pagina,
# nao eh timeout dos elementos.
driver.set_page_load_timeout(10)

# exemplos de elementos de busca de forma explicita.
driver.find_element_by_id("user_name")
driver.find_element_by_class_name("new_user")
driver.find_element_by_css_selector("#user_lastname")
driver.find_element_by_xpath("//*[@id=\"user_lastname\"]")
driver.find_element_by_name("user[email]")
driver.find_element_by_link_text("Treinamento")
driver.find_element_by_partial_link_text("Busca de")
print(driver.current_url)
#print(driver.page_source)
print(driver.title)
driver.quit()
