---
hide_title: true
title: Timeout when launching Windows application
---

# <a id="troubleshooting-2362" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Timeout when launching Windows application

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you reach timeout when launching Windows applications, try one of the following ways:</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><ol className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Close all unneeded apps and opened folders. Open Katalon
          Studio only.</span></li><li className="li step stepexpand"><span className="ph cmd">Remove unused shortcuts on your desktop and your taskbar.</span></li><li className="li step stepexpand"><span className="ph cmd">Use <code className="ph codeph">Windows.startApplication(…)</code> instead of <code className="ph codeph">Windows.startApplicationWithTitle(…)</code>.</span><div className="itemgroup info"><p className="p">For example:</p><pre className="pre codeblock"><code>Windows.startApplication('C:\\Users\\katalon\\Desktop\\Demo\\WindowsFormsApp.exe') Windows.switchToWindowTitle('Main App Title') // Replace this by your main window title</code></pre></div></li></ol></section></div>
