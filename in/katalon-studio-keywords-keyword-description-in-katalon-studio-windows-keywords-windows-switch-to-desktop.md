---
hide_title: true
title: '[Windows] Switch To Desktop'
---

# <a id="topic-6770" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Switch To Desktop


## Description

                        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Switch from the current running driver to a desktop session of the Windows Driver. This keyword initializes another Windows Driver with the <span className="ph uicontrol">app: Root </span>(the whole desktop) desired capability and the same WinAppDriver URL and Proxy settings of the application driver. </p> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">All of Windows built-in keywords now are manipulated by the desktop Windows Driver.</p> 
                                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">switchToDesktop</code></p> 
                        

## Example

                        
<div xmlns="http://www.w3.org/1999/xhtml" className="p">
  <pre className="pre codeblock"><code>"Start the note pad application"{"\n"}Windows.startApplication('C:\\Windows\\System32\\notepad.exe'){"\n"}{"\n"}"Switch to control the Desktop"{"\n"}Windows.switchToDesktop()</code></pre>
</div>
        
