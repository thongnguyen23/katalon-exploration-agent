---
hide_title: true
title: Handle WebDrivers with EventFiringWebDriver in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handle WebDrivers with EventFiringWebDriver in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can use the Selenium-based class <code className="ph codeph">EventFiringWebDriver</code> to configure event-driven capabilities related to your WebDrivers for test execution.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This can be used for example when logging steps or triggering certain events before an operation. You can learn more about this class from the Selenium documentation here: <a className="xref j-external-link" href="https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/support/events/EventFiringWebDriver.html" target="_blank">EventFiringWebDriver</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this article, we show you how to handle WebDrivers with the support of <code className="ph codeph">EventFiringWebDriver</code>.</p> 

## <a id="id_1" class="anchor_top_offset"/>Use WebDriver Event Listeners

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can use <code className="ph codeph">WebDriverEventListener</code> to handle events   started by the WebDriver, which happens for example, before or   after navigation, before or after a click. If   <code className="ph codeph">EventFiringWebDriver</code> is a class that wraps around the   WebDriver to throw events, <code className="ph codeph">WebDriverEventListeners</code> is   an interface to catch WebDriver events. You can learn more about   this interface from the Selenium documentation here: <a className="xref j-external-link" href="https://seleniumhq.github.io/selenium/docs/api/java/org/openqa/selenium/support/events/WebDriverEventListener.html" target="_blank">WebDriverEventListener</a> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Below is an example use of a custom   <code className="ph codeph">WebDriverEventListener</code>:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Create a new package to contain a keyword. Go to <strong className="ph b">File       &gt; New &gt; Package</strong>. Here, we name the package     <strong className="ph b">customkeyword</strong>.</li><li className="li">     <p className="p">Create a new keyword to handle WebDriver events.</p>     <ul className="ul"><li className="li">Go to <strong className="ph b">File &gt; New &gt; Keywords</strong>. A         <strong className="ph b">New</strong> dialog opens.</li><li className="li">         <p className="p">Click <strong className="ph b">Browse</strong> to choose a package for your           keyword, then manually type the class name. Here, we choose the           package created from Step 1 and name the keyword           <strong className="ph b">MyCustomWebEventListener</strong>. Click           <strong className="ph b">OK</strong>. A new keyword page opens.</p>         <p className="p">           <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/handle-webdrivers/KS-WEBDRIVER-Choose-package-and-name-the-keyword.png")} width={600} alt="Choose the package and create the keyword" /><br /><br />         </p>       </li><li className="li">         <p className="p">Copy and paste below sample code into the created keyword.</p>         <pre className="pre codeblock"><code>import org.openqa.selenium.WebDriver{"\n"}import org.openqa.selenium.support.events.AbstractWebDriverEventListener{"\n"}{"\n"}public class MyCustomWebEventListener extends AbstractWebDriverEventListener {"{"}{"\n"}{"    "}@Override{"\n"}{"    "}public void beforeNavigateTo(String url, WebDriver driver) {"{"}{"\n"}{"        "}println "Before navigating to " + url;{"\n"}{"    "}{"}"}{"\n"}{"}"}{"\n"}</code></pre>         <p className="p">           <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/handle-webdrivers/KS-WEBDRIVER-final-results-after-creating-the-keyword.png")} width={500} alt="Final results after creating the keyword" /><br /><br />         </p>       </li></ul>   </li><li className="li">     <p className="p">Open your test script. To register       <code className="ph codeph">MyCustomWebEventListener</code> with WebDriver, copy and       paste the sample code as below:</p>     <pre className="pre codeblock"><code>import org.openqa.selenium.WebDriver as WebDriver{"\n"}import org.openqa.selenium.support.events.EventFiringWebDriver as EventFiringWebDriver{"\n"}{"\n"}import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory{"\n"}import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI{"\n"}{"\n"}import customlistener.MyCustomWebEventListener as MyCustomWebEventListener{"\n"}{"\n"}WebUI.openBrowser(''){"\n"}{"\n"}WebDriver webdriver = DriverFactory.getWebDriver(){"\n"}{"\n"}EventFiringWebDriver eventFiring = ((webdriver) as EventFiringWebDriver){"\n"}{"\n"}eventFiring.register(new MyCustomWebEventListener()){"\n"}{"\n"}DriverFactory.changeWebDriver(eventFiring){"\n"}{"\n"}WebUI.navigateToUrl('www.google.com'){"\n"}{"\n"}WebUI.closeBrowser(){"\n"}</code></pre>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/handle-webdrivers/KS-WEBDRIVER-Results-after-registering-custom-keyword.png")} width={500} alt="Final results after registering the keyword" /><br /><br />     </p>   </li><li className="li">     <p className="p">Hit <strong className="ph b">Run</strong>, then observe the result in the Console       log.</p>     <pre className="pre codeblock"><code>2021-09-13 09:16:21.722 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- sessionId = ebf7a901164241457b656ffece5da9b0{"\n"}2021-09-13 09:16:21.747 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- browser = Chrome 93.0.4577.63{"\n"}2021-09-13 09:16:21.753 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- platform = Mac OS X{"\n"}2021-09-13 09:16:21.754 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- seleniumVersion = 3.141.59{"\n"}2021-09-13 09:16:21.773 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- proxyInformation = ProxyInformation {"{"} proxyOption=NO_PROXY, proxyServerType=HTTP, username=, password=********, proxyServerAddress=, proxyServerPort=0, executionList="", isApplyToDesiredCapabilities=true {"}"}{"\n"}2021-09-13 09:16:22.642 DEBUG testcase.WebDriver Event Listeners{"       "}- 2: webdriver = getWebDriver(){"\n"}2021-09-13 09:16:22.652 DEBUG testcase.WebDriver Event Listeners{"       "}- 3: eventFiring = webdriver{"\n"}2021-09-13 09:16:22.673 DEBUG testcase.WebDriver Event Listeners{"       "}- 4: eventFiring.register(new customlistener.MyCustomWebEventListener()){"\n"}2021-09-13 09:16:22.693 DEBUG testcase.WebDriver Event Listeners{"       "}- 5: changeWebDriver(eventFiring){"\n"}2021-09-13 09:16:22.699 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- sessionId = ebf7a901164241457b656ffece5da9b0{"\n"}2021-09-13 09:16:22.711 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- browser = Chrome 93.0.4577.63{"\n"}2021-09-13 09:16:22.711 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- platform = Mac OS X{"\n"}2021-09-13 09:16:22.712 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- seleniumVersion = 3.141.59{"\n"}2021-09-13 09:16:22.713 INFO{"  "}c.k.k.core.webui.driver.DriverFactory{"    "}- proxyInformation = ProxyInformation {"{"} proxyOption=NO_PROXY, proxyServerType=HTTP, username=, password=********, proxyServerAddress=, proxyServerPort=0, executionList="", isApplyToDesiredCapabilities=true {"}"}{"\n"}2021-09-13 09:16:22.722 DEBUG testcase.WebDriver Event Listeners{"       "}- 6: navigateToUrl("www.google.com"){"\n"}Before navigating to http://www.google.com{"\n"}2021-09-13 09:16:23.220 DEBUG testcase.WebDriver Event Listeners{"       "}- 7: closeBrowser(){"\n"}2021-09-13 09:16:23.243 INFO{"  "}c.k.katalon.core.main.TestCaseExecutor{"   "}- END Test Cases/WebDriver Event Listeners{"\n"}</code></pre>   </li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Use RemoteWebDriver

Because EventFiringWebDriver does not implement the interface RemoteWebDriver, to obtain a RemoteWebDriver instance safely, do as follows:

```jsx
....
// Cast Katalon's WebDriver into EventFiringWebDriver
EventFiringWebDriver eventFiring = (EventFiringWebDriver) DriverFactory.getWebDriver()
// Get the driver wrapped inside
WebDriver wrappedWebDriver = eventFiring.getWrappedDriver()
// Cast the wrapped driver into RemoteWebDriver
RemoteWebDriver katalonWebDriver = (RemoteWebDriver) wrappedWebDriver
// Katalon now uses RemoteWebDriver instead of your local driver
```

We recommend encapsulating the above logic into a function to avoid code duplication.

:::info notes
This is to avoid an exception in the case that your code is casting the WebDriver from DriverFactory, such as with:

```jsx
....
RemoteWebDriver katalonWebDriver = (RemoteWebDriver) DriverFactory.getWebDriver()
```

In this scenario, from Katalon Studio 7.0.0, an exception would appear as below:

```jsx
Cannot cast object 'com.kms.katalon.core.webui.driver.SmartWaitWebDriver@7cab1508' with class 'com.kms.katalon.core.webui.driver.SmartWaitWebDriver' to class 'org.openqa.selenium.remote.RemoteWebDriver'
```

(From [Russ Thomas's bug report](https://forum.katalon.com/t/bug-katalon-v7-cannot-cast-smartwaitwebdriver-to-remotewebdriver/33236))
:::

## <a id="id_3" class="anchor_top_offset"/>See also

    
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/web-testing/handle-webdrivers/upgrade-or-downgrade-webdrivers-in-katalon-studio">Update       or Downgrade WebDrivers</a>   </li>   <li className="li">     <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/web-testing/handle-webdrivers/terminate-webdrivers-in-katalon-studio">Terminate       Webdrivers</a>   </li> </ul> 
    
  
