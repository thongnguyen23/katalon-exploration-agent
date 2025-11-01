---
hide_title: true
title: Encounter xcodebuild exited with code '65' and signal 'null'
---

# <a id="troubleshooting-1152" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Encounter xcodebuild exited with code '65' and signal 'null'

<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Your .ipa application and/or WebDriverAgent is not signed correctly.</p></section><section className="section remedy"><ol className="ol steps"><li className="li step"><span className="ph cmd">Sign and rebuild the WebDriverAgent XCode project with your developer certificate.</span></li><li className="li step"><span className="ph cmd">Uncheck <strong className="ph b">Automatically Signing</strong> option from WebDriverAgentRunner and select <strong className="ph b">valid provisioning profile</strong> (profile displayed as Eligible from the list).D</span></li></ol></section></div>
