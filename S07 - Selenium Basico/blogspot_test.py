    # -*- coding: utf-8 -*-
    from selenium import webdriver
    from selenium.webdriver.support.select import Select
     
    # Vai criar a instancia do driver usando o driver do firefox.
    driver = webdriver.Firefox()
     
    # Link da nossa url
    base_url = "http://reinaldorossetti.blogspot.com.br"
     
    # Vai carregar a url no browser.
    driver.get(base_url + "/")
     
    # Espera implicita de 60s se demorar mais que isso vai dar erro.
    driver.implicitly_wait(60)
     
    # Vai pesquisar o elemento link que contem o texto abaixo.
    test = driver.find_element_by_link_text("Como corrigir no Ruby certificate verify failed")
     
    # Vou dar o clique nesse elemento.
    test.click()
     
    # Espera implicita de 60s, para carregar a nova página, se demorar mais que isso vai dar erro.
    driver.implicitly_wait(60)
     
    # Vai fazer a mudaça de frame na página.
    driver.switch_to.frame("comment-editor")
     
    # Vai pegar o elemento via id, caso der erro, é porque não localizou o elemento esperado.
    elemento_commentario = driver.find_element_by_id("commentBodyField")
     
    # Vai limpar o campo comentário antes de enviar o texto.
    elemento_commentario.clear()
     
    # Vai enviar o texto para o campo comentario.
    elemento_commentario.send_keys("post muito legal!")
     
    # Vai fazer o select, me trazendo a quantidade de opcoes, para fazer o assert.
    select = Select(driver.find_element_by_css_selector("#identityMenu"))
    select_test = select.options
    total = (len(select_test))
    print(total)
    assert (total == 9)
