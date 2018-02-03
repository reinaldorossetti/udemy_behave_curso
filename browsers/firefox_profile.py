from selenium import webdriver

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("network.proxy.type", 1)
firefox_profile.set_preference("network.proxy.http", "ncproxy1")  # set your ip
firefox_profile.set_preference("network.proxy.http_port", 8080)  # set your port
firefox_profile.set_preference("network.proxy.ssl", "ncproxy1")
firefox_profile.set_preference("network.proxy.ssl_port", 8080)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get("https://www.google.com")

