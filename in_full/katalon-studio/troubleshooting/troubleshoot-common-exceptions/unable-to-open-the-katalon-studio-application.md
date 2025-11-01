---
hide_title: true
title: Unable to open the Katalon Studio application
---

# <a id="troubleshooting-5477" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to open the Katalon Studio application

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><div className="p">You are unable to open the Katalon Studio application on Windows machine and might encounter the following error:<pre className="pre codeblock"><code>An error has occurred. See the log file{"\n"}C:\Users\Laxmi.Kadam\Downloads\Katalon Studio Windows_64-9.4.0\Kat{"\n"}alon_Studio_Windows_64-9.4.0\config\.metadata\log.</code></pre></div></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">This error happens the files are broken due to having some special characters.</p></section><section className="section remedy"><ol className="ol steps"><li className="li step stepexpand"><span className="ph cmd">You might need to remove the following items:</span><div className="itemgroup info"><ul className="ul"><li className="li">the <code className="ph codeph">config/.metadata</code> folder under the Katalon installation folder</li><li className="li">the <code className="ph codeph">application.properties</code> file under <code className="ph codeph">%userprofile%/.katalon</code> the folder</li></ul></div></li><li className="li step stepexpand"><span className="ph cmd">Try open the application again.</span></li></ol></section></div>
