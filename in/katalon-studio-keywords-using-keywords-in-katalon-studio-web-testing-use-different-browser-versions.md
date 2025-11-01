---
title: "Use different browser versions"
---

In case you want Katalon Studio to use different versions besides the currently installed version, there are two ways to do it: create custom keywords to set path to specific browser version, or manually update/downgrade your browser version.

### Create custom keywords

To use this method, the browser instances you wish to use should be installed on your machine first.

1. Create a custom keyword to open the browser. Press <kbd className="ph userinput">Ctrl + Shift + O</kbd> to automatically import necessary packages. To learn more about creating a custom keyword, you can refer to this document here: [Introduction to Custom Keyword](katalon-studio/keywords/custom-keywords/introduction-to-custom-keywords-in-katalon-studio).

2. Provide the correct paths for `firefoxPath`, `firefoxDriver`, `chromeDriverPath`, and `chromePath` in the following sample code. For example, on a Windows machine:
   - `firefoxPath` value is `C:\\Program Files\\Mozilla Firefox\\firefox.exe`
   - `firefoxDriver` value is `C:\Katalon_Studio\configuration\resources\drivers\firefox_win64\geckodriver.exe`
```jsx
import com.kms.katalon.core.webui.driver.DriverFactory
import org.openqa.selenium.WebDriver
import org.openqa.selenium.firefox.FirefoxDriver
import org.openqa.selenium.chrome.ChromeDriver
import org.openqa.selenium.chrome.ChromeOptions
import com.kms.katalon.core.annotation.Keyword

public class WebUICustomKeywords {  
    @Keyword  
    def openFirefoxBrowser(String firefoxPath, String firefoxDriver) { 
    // Set path to Firefox version 
    System.setProperty("webdriver.firefox.bin", firefoxPath) 

    // Set path to Firefox driver
    System.setProperty("webdriver.gecko.driver", firefoxDriver)

    WebDriver driver = new FirefoxDriver() 
    DriverFactory.changeWebDriver(driver)  
    }  

    @Keyword  
    def openChromeBrowser(String chromeDriverPath, String chromePath) { 
    // Set path to Chrome driver
    System.setProperty("webdriver.chrome.driver", chromeDriverPath) 

    ChromeOptions options = new ChromeOptions() 

    // Set path to Chrome binary
    options.setBinary(chromePath) 

    WebDriver driver = new ChromeDriver(options) 
    DriverFactory.changeWebDriver(driver)  
    } 	
}
```

3. Use the custom keyword in your test case.

```jsx
CustomKeywords.'com.example.WebUICustomKeywords.openFirefoxBrowser'('C:\\Program Files\\Mozilla Firefox\\firefox.exe','C:\Katalon_Studio\configuration\resources\drivers\firefox_win64\geckodriver.exe')

WebUI.navigateToUrl(GlobalVariable.G_SiteURL) 
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))
```

### Downgrade browser version

If you want to use a very old version of your current browser, you might need to downgrade or upgrade browser drivers as well as Selenium WebDriver. Refer to this document for further instruction: [Update or Downgrade WebDrivers](/katalon-studio/manage-projects/set-up-projects/web-testing/handle-webdrivers/upgrade-or-downgrade-webdrivers-in-katalon-studio).
