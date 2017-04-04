var webdriver = require('selenium-webdriver');

var driver = new webdriver.Builder()
	.forBrowser('chrome')
	.build();

driver.get('http://www.google.com/ncr');
driver.findElement(webdriver.By.name('q')).sendKeys('webdriver');
driver.findElement(webdriver.By.name('btnG')).click();
driver.wait(webdriver.until.titleIs('webdriver - Google Search'), 1000);
console.log(driver.title);