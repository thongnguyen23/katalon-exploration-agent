---
hide_title: true
title: Retrieve mobile's session in Katalon Studio
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Retrieve mobile's session in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To get current mobile's session after using 'Start Application' built-in keyword, use the sample code below:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import org.openqa.selenium.WebDriver{"\n"}import org.openqa.selenium.WebElement{"\n"}import com.kms.katalon.core.annotation.Keyword{"\n"}import com.kms.katalon.core.mobile.helper.MobileElementCommonHelper{"\n"}import com.kms.katalon.core.mobile.keyword.internal.MobileDriverFactory{"\n"}import com.kms.katalon.core.testobject.TestObject{"\n"}import com.kms.katalon.core.util.KeywordUtil{"\n"}import io.appium.java_client.AppiumDriver {"\n"}{"\n"}Mobile.startApplication("Your Application", false){"\n"}AppiumDriver&lt;?&gt; driver = MobileDriverFactory.getDriver(){"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">References:</strong></p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><a className="xref j-external-link" href="http://docs.katalon.com/display/KD/%5BMobile%5D+Start+Application" target="_blank">Start Application</a></li></ul> 
