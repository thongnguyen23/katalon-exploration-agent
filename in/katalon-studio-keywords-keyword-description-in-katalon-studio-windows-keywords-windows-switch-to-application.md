---
hide_title: true
title: '[Windows] Switch To Application'
---

# <a id="topic-5019" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Switch To Application


## Description

                        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Switch from the current running driver to the application Windows Driver.</p> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">switchToApplication</code></p> 
        

## Example

                        
<div xmlns="http://www.w3.org/1999/xhtml" className="p">
  <pre className="pre codeblock"><code>"Start the note pad application"{"\n"}Windows.startApplication('C:\\Windows\\System32\\notepad.exe'){"\n"}{"\n"}"Switch to control the desktop"{"\n"}Windows.switchToDesktop(){"\n"}{"\n"}// Do some stuffs with the desktop{"\n"}{"\n"}"Switch back to control the note pad application"{"\n"}Windows.switchToApplication()</code></pre>
</div>
        
