---
hide_title: true
title: Xcode fails to create a provisioning profile for the WebDriverAgentRunner target
---

# <a id="troubleshooting-2013" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Xcode fails to create a provisioning profile for the WebDriverAgentRunner target

<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><div className="li step p"><span className="ph cmd">This necessitates manually changing the bundle id for the target by going into the <strong className="ph b">Build Settings</strong> tab, and changing the <strong className="ph b">Product Bundle Identifier</strong> from <code className="ph codeph">com.facebook.WebDriverAgentRunner</code> to something that Xcode will accept.</span></div></section></div>
