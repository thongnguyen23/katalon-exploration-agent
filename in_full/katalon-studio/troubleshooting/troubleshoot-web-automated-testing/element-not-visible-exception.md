---
hide_title: true
title: Element not visible exception
---

# <a id="troubleshooting-1490" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Element not visible exception

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you encounter the following exception: <code className="ph codeph">selenium.ElementNotVisibleException: Element is not currently visible and so may not be interacted.</code></p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><div className="li step p"><span className="ph cmd">Add the <code className="ph codeph">Wait For Element Visible</code> keyword before the one having this issue. To learn more about the <code className="ph codeph">Wait For Element Visible</code> keyword, you can refer to this document here: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-wait-for-element-visible">[WebUI] Wait For Element Visible</a>. </span><div className="itemgroup stepxmp"><pre className="pre codeblock"><code>WebUI.openBrowser('http://demoaut.katalon.com'){"\n"}WebUI.waitForElementVisible(findtestObject('btn_Login'),30){"\n"}WebUI.click(findTestObject('btn_Login'))</code></pre></div></div></section></div>
