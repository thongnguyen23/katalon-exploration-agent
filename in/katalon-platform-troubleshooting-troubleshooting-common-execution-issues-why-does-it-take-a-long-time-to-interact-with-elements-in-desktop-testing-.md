---
hide_title: true
title: Why does it take a long time to interact with elements in desktop testing ?
---

# <a id="troubleshooting-9136" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Why does it take a long time to interact with elements in desktop testing ?

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">Switching from one page to another page takes too much time. How to reduce the time switching the windows?</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Windows testing in <span className="ph">Katalon Studio</span> is based on Microsoft's <a className="xref j-external-link" href="https://github.com/microsoft/WinAppDriver">WinAppDriver</a>. Generally, here are the steps that Appium needs to go through to switch windows: </p><ol className="ol"><li className="li"><p className="p">Scan windows and create a source map</p></li><li className="li"><p className="p">Apply the object's locator to search</p></li><li className="li"><p className="p">Winappdriver will apply the command on the desktop application</p></li></ol><p className="p">That's the reason why it takes a certain amount of  time when switching windows.</p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">To reduce time when switching windows, we recommend you turn off unnecessary applications and update to the <a className="xref j-external-link" href="https://github.com/microsoft/WinAppDriver/releases" target="_blank">latest version of WinAppDriver</a>. </span></div></section></div>
