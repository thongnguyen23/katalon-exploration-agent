---
hide_title: true
title: Install Chrome extensions at runtime in Katalon Studio
---

# Install Chrome extensions at runtime in Katalon Studio

To install Chrome extensions before you start the browser, you can either use packed or unpacked extensions. The sample code below refer to packed extensions: 

```jsx
import org.openqa.selenium.WebDriver
import org.openqa.selenium.chrome.ChromeDriver
import org.openqa.selenium.chrome.ChromeOptions
import org.openqa.selenium.remote.DesiredCapabilities
import com.kms.katalon.core.webui.driver.DriverFactory

System.setProperty("webdriver.chrome.driver", "C:\Users\usuario\katalon\Test\Driver\chromedriver.exe");
ChromeOptions options = new ChromeOptions()
options.addExtensions(new File("C:\Users\usuario\Desktop\Firma-con-token.crx"))
DesiredCapabilities capabilities = new DesiredCapabilities()
capabilities.setCapability(ChromeOptions.CAPABILITY, options)
WebDriver driver = new ChromeDriver(capabilities)
DriverFactory.changeWebDriver(driver)
```

If you want to use unpacked extensions, refer to this page: [Chrome Extensions](https://developer.chrome.com/docs/chromedriver/extensions).

References:
- [DriverFactory](https://api-docs.katalon.com/com/kms/katalon/core/webui/driver/DriverFactory.html)
- [Chrome desired capabilities](http://chromedriver.chromium.org/capabilities)
- [Install Chrome extensions](https://sites.google.com/a/chromium.org/chromedriver/extensions)
