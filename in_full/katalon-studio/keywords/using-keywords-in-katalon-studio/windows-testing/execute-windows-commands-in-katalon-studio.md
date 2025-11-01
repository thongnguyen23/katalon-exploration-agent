---
hide_title: true
title: Execute Windows commands in Katalon Studio
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Execute Windows commands in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To execute Windows command line, simply use this script in your   test case:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>String cmd = "Your command"{"\n"}Runtime.getRuntime().exec(cmd){"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Example:</strong> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Call taskkill command</li></ul> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>String cmd = "taskkill /F firefox.exe"{"\n"}Runtime.getRuntime().exec(cmd){"\n"}</code></pre> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Launch external program:</li></ul> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>Runtime.runtime.exec("path/to/vlc.exe"){"\n"}</code></pre> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Execute a batch file</li></ul> 

```jsx
import com.kms.katalon.core.configuration.RunConfiguration
  /**
   * Execute a batch file situated in the KS project directory.
   * @param batchFile (String) e.g. "myfile.bat"
   */
  static void runBatchFile(String batchFile) {
    String bf = RunConfiguration.getProjectDir() + '/' + batchFile
    comment("Running batch file: " + bf)
    Runtime.runtime.exec(bf)
  }
```    

## <a id="id_1" class="anchor_top_offset"/>References
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <p className="p">       <a className="xref j-external-link" href="https://api-docs.katalon.com/com/kms/katalon/core/configuration/RunConfiguration.html" target="_blank">RunConfiguration</a>     </p>   </li>   <li className="li">     <p className="p">       <a className="xref j-external-link" href="https://docs.oracle.com/javase/7/docs/api/java/lang/Runtime.html" target="_blank">Runtime</a>     </p>   </li>   <li className="li">     <a className="xref j-external-link" href="https://www.lifewire.com/list-of-command-prompt-commands-4092302" target="_blank">Windows       command line</a>   </li> </ul> 
    
  
