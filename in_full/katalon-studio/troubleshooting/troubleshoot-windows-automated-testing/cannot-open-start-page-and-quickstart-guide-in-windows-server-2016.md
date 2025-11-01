---
hide_title: true
title: Cannot open Start Page and Quickstart guide in Windows Server 2016
---

# <a id="troubleshooting-1547" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Cannot open Start Page and Quickstart guide in Windows Server 2016

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you are using Windows Server 2016 and encounter the following error:</p><p className="p"><code className="ph codeph">org.eclipse.swt.SWTError: Not implemented [WebView2 runtime not found]</code></p><p className="p">You might not be able to open Start Page and Quickstart guide.</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p"> This is due to the Windows Server 2016 machine not having WebView2 Runtime, which is required for Katalon Studio to open the Start Page and Quickstart guide. This can be resolved by  installing  WebView2 Runtime on your machine. Do as follows:</p></section><section className="section remedy"><ol className="ol steps"><li className="li step"><span className="ph cmd">Go to <a className="xref j-external-link" href="https://developer.microsoft.com/en-us/microsoft-edge/webview2/#download-section" target="_blank">WebView2 - Microsoft Edge Developer</a>.</span></li><li className="li step"><span className="ph cmd">Follow the instructions and download the suitable installer depending on your preference.</span></li></ol></section></div>
