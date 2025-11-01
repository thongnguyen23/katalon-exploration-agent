---
hide_title: true
title: An unknown server-side error occurred while processing the command
---

# <a id="troubleshooting-1698" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>An unknown server-side error occurred while processing the command

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you encounter the error <code className="ph codeph">java.util.concurrent.ExecutionException: org.openqa.selenium.WebDriverException: An unknown server-side error occurred while processing the command</code>. </p><p className="p">Original error: <code className="ph codeph">Could not proxy command to the remote server</code>. </p><p className="p">Original error: <code className="ph codeph">timeout of 240000ms exceeded</code>.</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><ol className="ol steps"><li className="li step"><span className="ph cmd">Install <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/ios/mobile-install-webdriveragent-for-real-ios-devices-in-katalon-studio">Webdriveragent</a>.</span></li><li className="li step"><span className="ph cmd">Kill the running appium proccesses with the following command: <code className="ph codeph">killall -9 node</code>.</span></li><li className="li step"><span className="ph cmd">Start the AUT again.</span></li></ol></section></div>
