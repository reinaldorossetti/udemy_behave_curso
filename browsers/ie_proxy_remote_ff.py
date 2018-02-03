from selenium import webdriver
from selenium.webdriver.common.proxy import *

myProxy = "host:8080"

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '',  # set this value as desired
    'socksUsername': '',
    'socksPassword': '',
})

driver = webdriver.Firefox(proxy=proxy)

# for remote
caps = webdriver.DesiredCapabilities.FIREFOX.copy()
proxy.add_to_capabilities(caps)

driver = webdriver.Remote(desired_capabilities=caps)

