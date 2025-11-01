---
hide_title: true
title: Illegal option specification exception
---

# <a id="troubleshooting-264" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Illegal option specification exception

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When executing in console mode, you can encounter the following error: <code className="ph codeph">joptsimple.IllegalOptionSpecificationException: $ is not a legal option character</code>.</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">This is because the name of your global variables might contain special characters like <code className="ph codeph">$</code>, or a space. For instance: </p><ul className="ul"><li className="li">Supported: <code className="ph codeph">-g_myVar="test"</code></li><li className="li">Not supported: <code className="ph codeph">-g_$myVar="test"</code></li></ul></section><section className="section remedy"><div className="li step p"><span className="ph cmd">To solve this issue, we recommend giving global variables a name without <code className="ph codeph">$</code>, and/or space.</span></div></section></div>
