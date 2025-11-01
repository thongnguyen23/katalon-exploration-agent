---
hide_title: true
title: Unable to detect all elements during mobile testing on BrowserStack
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-a0d1kjwg" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to detect all elements during mobile testing on BrowserStack

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When running mobile tests on BrowserStack, Katalon Studio may fail to detect all elements during test execution.</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Starting from Katalon Studio version 10.x, the supported Appium version is 2.x. However, the default Appium version on BrowserStack is 1.x. This mismatch between the two Appium versions causes the issue.</p><p className="p">To resolve the issue, you need to define the Appium version in your project settings. Follow these steps:</p></section><section className="section remedy"><ol className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph menucascade"><span className="ph uicontrol">Project Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Desired Capabilities</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Remote</span></span>.</span></li><li className="li step stepexpand"><span className="ph cmd">Add the following configurations.</span><div className="itemgroup info"><p className="p"><img className="image" width={700} src={useBaseUrl("/458887cd-576b-44ba-851c-ac62bf46a2eb/edit-browserstack-appium.png")} /></p><p className="p">Ensure that you specify the Appium version under <code className="ph codeph">bstack:options</code>.</p><p className="p">As an example, set the Appium version to <code className="ph codeph">2.6.0</code> to resolve the compatibility issue.</p></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">OK</span> to save changes.</span></li></ol></section></div>
