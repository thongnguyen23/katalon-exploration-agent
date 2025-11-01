---
hide_title: true
title: Invalid element state exception
---

# <a id="troubleshooting-2053" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Invalid element state exception

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you encounter the following exception: <code className="ph codeph">org.openqa.selenium.InvalidElementStateException: invalid element state: Element is not currently interactable and may not be manipulated.</code></p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><div className="li step p"><span className="ph cmd">Try one of the following solutions to resolve the issue:</span><div className="itemgroup info">Wait until the element is visible.</div><div className="itemgroup info">OR</div><div className="itemgroup info">Set a value directly using JavaScript.<pre className="pre codeblock"><code>import com.kms.katalon.core.webui.common.WebUiCommonHelper {"\n"}WebElement element = WebUiCommonHelper.findWebElement(findTestObject('your/object'),30){"\n"}WebUI.executeJavaScript("arguments[0].value='Your Value'", Arrays.asList(element))</code></pre></div></div></section></div>
