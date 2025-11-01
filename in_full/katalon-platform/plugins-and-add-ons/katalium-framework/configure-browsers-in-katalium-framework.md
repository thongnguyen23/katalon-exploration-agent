---
hide_title: true
title: Configure Browsers in Katalium Framework
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Configure Browsers in Katalium Framework

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalium Framework provides four default browser configurations:   <code className="ph codeph">chrome</code>, <code className="ph codeph">firefox</code>,   <code className="ph codeph">internet_explorer</code>, <code className="ph codeph">edge</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can specify the default browser in the file   <code className="ph codeph">kata-default.properties</code> (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/resources/kata-default.properties" target="_blank">sample</a>).   It can also be overridden using the parameter   <code className="ph codeph">kataBrowser</code>, e.g. <code className="ph codeph">mvn clean test     -DkataBrowser=firefox</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here is a simple definition of two test suites that run   parallelly on Chrome and Firefox (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/resources/testng-parallel.xml" target="_blank">source     code</a>):</p> 

```jsx
<?xml version = "1.0" encoding = "UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="Suite1" verbose="1" parallel="tests" thread-count="2" >
    <test name="simple" >
        <parameter name="kataScreenshot" value="true" />
        <parameter name="kataBrowser" value="firefox" />
        <classes>
            <class name="com.katalon.kata.sample.simple.MakeAppointmentTest" />
        </classes>
    </test>
    <test name="parameterize" >
        <parameter name="kataScreenshot" value="true" />
        <parameter name="kataBrowser" value="chrome" />
        <parameter name="facility" value="Hongkong CURA Healthcare Center" />
        <parameter name="visitDate" value="27/12/2016" />
        <parameter name="comment" value="Please make appointment as soon as possible." />
        <classes>
            <class name="com.katalon.kata.sample.parameterize.ParameterizedMakeAppointmentTest" />
        </classes>
    </test>
</suite>
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Custom browsers can be provided by implementing the interface   <code className="ph codeph">com.katalon.kata.webdriver.WebDriverFactory</code>. The   following example is a factory that creates a Sauce Labs WebDriver   instance (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/java/com/katalon/kata/sample/custombrowser/SampleSauceLabsWebDriverFactory.java" target="_blank">source     code</a>):</p> 

```jsx
package com.katalon.kata.sample.custombrowser;

import com.katalon.kata.helper.ExceptionHelper;
import com.katalon.kata.helper.ParameterHelper;
import com.katalon.kata.webdriver.WebDriverFactory;
import org.apache.commons.lang3.StringUtils;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import java.net.URL;

public class SampleSauceLabsWebDriverFactory implements WebDriverFactory {
    private static final String BROWSER_KEY = "sauceBrowser";
    private static final String VERSION_KEY = "sauceBrowserVersion";
    private static final String PLATFORM_KEY = "saucePlatform";
    private static final String SAUCE_USER_NAME_KEY = "sauceUsername";
    private static final String SAUCE_ACCESS_KEY_KEY = "sauceAccessKey";
    private static final String SAUCE_URL = "https://ondemand.saucelabs.com/wd/hub";
    
    @Override
    public RemoteWebDriver createRemoteWebDriver(String seleniumServer) {

        try {

            String sauceUserName = ParameterHelper.getParameterDefaultValue(SAUCE_USER_NAME_KEY);
            String sauceAccessKey = ParameterHelper.getParameterDefaultValue(SAUCE_ACCESS_KEY_KEY);

            String browser = ParameterHelper.getParameterDefaultValue(BROWSER_KEY);
            String version = ParameterHelper.getParameterDefaultValue(VERSION_KEY);
            String os = ParameterHelper.getParameterDefaultValue(PLATFORM_KEY);

            if (StringUtils.isBlank(browser)) {
                browser = "chrome";
            }
            if (StringUtils.isBlank(version)) {
                version = "latest";
            }
            if (StringUtils.isBlank(os)) {
                os = "Windows 10";
            }

            DesiredCapabilities capabilities = new DesiredCapabilities();
            capabilities.setCapability("username", sauceUserName);
            capabilities.setCapability("accessKey", sauceAccessKey);
            capabilities.setCapability(CapabilityType.BROWSER_NAME, browser);
            capabilities.setCapability(CapabilityType.VERSION, version);
            capabilities.setCapability(CapabilityType.PLATFORM, os);

            RemoteWebDriver driver = new RemoteWebDriver(new URL(SAUCE_URL), capabilities);
            return driver;

        } catch (Exception e) {
            return ExceptionHelper.rethrow(e);
        }
    }
}
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Browser factories need to be registed with the   <code className="ph codeph">WebDriverPool</code>, e.g. (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/java/com/katalon/kata/sample/custombrowser/RegisterCustomBrowsersListener.java" target="_blank">source     code</a>):</p> 

```jsx
package com.katalon.kata.sample.custombrowser;

import com.katalon.kata.webdriver.WebDriverPool;
import org.testng.IExecutionListener;

public class RegisterCustomBrowsersListener implements IExecutionListener {

    private static final String SAUCE_LABS_BROWSER = "saucelabs";

    @Override
    public void onExecutionStart() {
        WebDriverPool webDriverPool = WebDriverPool.get();
        webDriverPool.setFactory(SAUCE_LABS_BROWSER, new SampleSauceLabsWebDriverFactory());
    }

    @Override
    public void onExecutionFinish() {

    }
}
```