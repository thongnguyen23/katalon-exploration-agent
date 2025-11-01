---
hide_title: true
title: Element click intercepted exception
---

# <a id="troubleshooting-9116" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Element click intercepted exception

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you encounter the following exception: <code className="ph codeph">org.openqa.selenium.ElementClickInterceptedException: element click intercepted: Element is not clickable at point</code></p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><ol className="ol steps"><li className="li step"><span className="ph cmd">If the test case fails because there is another object covering the target element, for example, a pop-up dialog, you can add actions to remove the object before the <span className="ph uicontrol">Click </span>action.</span></li><li className="li step"><span className="ph cmd">If the <span className="ph uicontrol">Default wait for element timeout</span> setting is not long enough for Katalon to click on the target element behind an overlay, you can add the <code className="ph codeph">WebUI.waitForElementClickable</code> keyword before the <span className="ph uicontrol">Click</span> action. To learn more about using the <code className="ph codeph">WebUI.waitForElementClickable</code> keyword, you can refer to this document here: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-wait-for-element-clickable">[WebUI] Wait For Element Clickable</a>.</span></li></ol></section></div>
