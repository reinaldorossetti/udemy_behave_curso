from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

chrome_options = Options()
download_para = "C:\\Users\\reiload\\PycharmProjects\\udemy_my_course\\"
profile = {"plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}],
    "download.default_directory" : download_para}

chrome_options.add_argument("--disable-web-security")
chrome_options.add_experimental_option("prefs",profile)
d = webdriver.Chrome(chrome_options=chrome_options)

d.get('http://www.delboniauriemo.com.br')

d.set_page_load_timeout(10)
d.implicitly_wait(3)

user_elem= '#form-fap-password #code'
password_elem= '#password'
submit_elem= '#form-fap-password button[title="Ok"]'
modal= '#socialid-modal'
bt_ir_exame= '#socialid-modal button[title*="meus exames"]'
pesquisa_analise= 'span[onclick*="exibirDetalhes"]'
visualizar_pdf= '.botaoDownload img'
selecionar_clicose= 'input[name="produtosSelecionados"]'
download= 'button[id=download]'


d.find_element_by_css_selector(user_elem).send_keys("")
d.find_element_by_css_selector(password_elem).send_keys("")
d.find_element_by_css_selector(submit_elem).click()
d.find_element_by_css_selector(bt_ir_exame).click()

d.switch_to.window(d.window_handles[-1])
WebDriverWait(d, 10).until(lambda d: d.find_element_by_css_selector(visualizar_pdf).is_displayed())
d.find_element_by_css_selector(visualizar_pdf).click()
d.switch_to.window(d.window_handles[-1])

def expand_shadow_element(element):
  shadow_root = d.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

d.switch_to.window(d.window_handles[1])

d.get('chrome://downloads/')

root1 = d.find_element_by_tag_name('downloads-manager')
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element_by_css_selector('iron-list#downloads-list')
shadow_root2 = expand_shadow_element(root2)

root3 = shadow_root1.find_element_by_css_selector('downloads-item')
shadow_root3 = expand_shadow_element(root3)

search_button = shadow_root3.find_element_by_css_selector("a[id=show]")
search_button.click()






