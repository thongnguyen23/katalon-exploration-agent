---
hide_title: true
title: Other Utilities in Katalium Framework
---

# <a id="id_katalium-framework-others" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Other Utilities in Katalium Framework


## <a id="id_1" class="anchor_top_offset"/>Parameterization

<p xmlns="http://www.w3.org/1999/xhtml" className="p">TestNG provides a comprehensive mechanism for customizing   parameters, which can be referred <a className="xref j-external-link" href="https://testng.org/doc/documentation-main.html#parameters" target="_blank">here</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Katalium Framework, you can set default values for parameters   in the file <code className="ph codeph">kata-default.properties</code> (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/resources/kata-default.properties" target="_blank">example</a>),   or using at runtime using Java's system properties, e.g. <code className="ph codeph">mvn     clean test -DkataBrowser=firefox</code>. This is very handy when   you do not want reconfigure unchanged parameters.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Default values of parameters can be accessed using the helper   <code className="ph codeph">com.katalon.kata.helper.ParameterHelper</code>.</p> 
    

## <a id="id_2" class="anchor_top_offset"/>Logging

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalium Framework provides the class   <code className="ph codeph">com.katalon.kata.helper.LogHelper</code> to help retrieve   <code className="ph codeph">org.slf4j.Logger</code> instances with correct class   names.</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>private static final Logger log = LogHelper.getLogger();{"\n"}</code></pre> 
                    
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>log.info("Open CURA home page.");{"\n"}</code></pre> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Sample output:</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>09:26:29.475 [main] INFO{"  "}com.katalon.kata.testng.TestTemplate - Make appointment with parameters{"\n"}09:26:29.475 [main] INFO{"  "}com.katalon.kata.testng.TestTemplate - Facility Hongkong CURA Healthcare Center{"\n"}09:26:29.476 [main] INFO{"  "}com.katalon.kata.testng.TestTemplate - VisitDate 27/12/2016{"\n"}09:26:29.476 [main] INFO{"  "}com.katalon.kata.testng.TestTemplate - Comment Please make appointment as soon as possible.{"\n"}09:26:29.476 [main] INFO{"  "}c.katalon.kata.selenium.PageTemplate - Open CURA home page.{"\n"}09:26:38.528 [main] INFO{"  "}c.katalon.kata.selenium.PageTemplate - Make appointment.{"\n"}</code></pre> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Logs will be printed out on the console and in TestNG XML   reports.</p> 
    
  

## <a id="id_3" class="anchor_top_offset"/>Capture WebDriver actions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can attach a custom <code className="ph codeph">org.openqa.selenium.support.events.AbstractWebDriverEventListener</code> to capture WebDriver events (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalium-sample/blob/master/src/test/java/com/katalon/kata/sample/listener/EventListener.java" target="_blank">source code</a>):</p> 

```jsx
package com.katalon.kata.sample.listener;

import com.katalon.kata.webdriver.WebDriverPool;
import org.testng.IExecutionListener;

public class EventListener implements IExecutionListener {
    @Override
    public void onExecutionStart() {
        WebDriverPool webDriverPool = WebDriverPool.get();
        webDriverPool.setAfterCreateDriverListener(
            driver -> { driver.register(new WebDriverEventListener()); });
    }

    @Override
    public void onExecutionFinish() {}
}
```