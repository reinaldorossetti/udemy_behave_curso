using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Support.UI;

class GoogleSearch
{
static void Main()
	{
		IWebDriver driver = new FirefoxDriver();
		driver.Navigate().GoToUrl("http://www.google.com");
		IWebElement query = driver.FindElement(By.Name("q"));
		query.SendKeys("Hello Selenium WebDriver!");
		query.Submit();
		Console.WriteLine(driver.Title);
	}
}