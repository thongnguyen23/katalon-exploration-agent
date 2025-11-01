---
hide_title: true
title: WebDriver Auto-update for Katalium Server
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>WebDriver Auto-update for Katalium Server

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When Katalium starts, the server will detect the installed   browsers and download the compatible WebDriver versions. Supported   browsers are Chrome, Firefox, Internet Explorer, and Edge (pre   18).</p> 
    

## <a id="id_1" class="anchor_top_offset"/>Install WebDriver for Microsoft Edge version 18 and newer

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Microsoft WebDriver for Microsoft Edge version 18 is a Windows   Feature on Demand.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To install run the following in an elevated command prompt:</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>DISM.exe /Online /Add-Capability /CapabilityName:Microsoft.WebDriver~~~~0.0.1.0{"\n"}</code></pre> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Please refer to <a className="xref j-external-link" href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/" target="_blank">here</a>   for more details.</p> 
    
  
