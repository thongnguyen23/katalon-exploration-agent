---
hide_title: true
title: Appium directory is not set
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-9558" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Appium directory is not set

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you encounter the following error <code className="ph codeph">com.kms.katalon.core.appium.exception.AppiumStartException: Appium directory is not set</code>.</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">When running tests with <strong className="ph b">Katalon Runtime Engine</strong>, by default Katalon checks the Appium directory at APPIUM_HOME environment variable. </p><ul className="ul"><li className="li">Windows: <span className="ph">C:\Users\AppData\Roaming\npm\node_modules\appium.</span>
      </li><li className="li">macOS and Linux: <span className="ph">/usr/local/lib/node_modules/appium</span>.</li></ul></section><section className="section remedy"><div className="li step p"><span className="ph cmd">To set Appium location by using APPIUM_HOME environment variable:</span><div className="itemgroup info">For Windows:</div><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/roubleshooting-automated-mobile-testing/windows-appium-home.png")} alt="Set Appium_Home for Windows" /><br /><br /></div><div className="itemgroup info">For macOS and Linux:<pre className="pre codeblock"><code>export APPIUM_HOME=/usr/local/lib/node_modules/appium</code></pre></div></div></section></div>
