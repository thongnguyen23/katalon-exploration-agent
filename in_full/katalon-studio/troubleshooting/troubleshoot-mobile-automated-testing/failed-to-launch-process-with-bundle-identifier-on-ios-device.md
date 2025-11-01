---
hide_title: true
title: Failed to launch process with bundle identifier on iOS device
---

# <a id="troubleshooting-9075" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Failed to launch process with bundle identifier on iOS device 

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><div className="p">Failed to launch process with bundle identifier such as <code className="ph codeph">com.johndoe.WebDriverAgentRunner.xctrunner</code>. Underlying Error: <pre className="pre codeblock"><code>The operation couldn't be completed. Unable to launch com.johndoe.WebDriverAgentRunner.xctrunner because it has an invalid code signature, inadequate entitlements or its profile has not been explicitly trusted by the user.</code></pre></div></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><ol className="ol steps"><li className="li step"><span className="ph cmd">On the iOS device, navigate to <span className="ph menucascade"><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">General</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Device Management</span></span>.</span></li><li className="li step"><span className="ph cmd">Trust the Apple Developement account displayed.</span></li></ol></section></div>
