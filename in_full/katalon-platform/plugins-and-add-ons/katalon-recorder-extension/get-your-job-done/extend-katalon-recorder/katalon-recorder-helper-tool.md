---
hide_title: true
title: Katalon Recorder Helper Tool
---

# <a id="id_katalon-recorder-helper-tool" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Katalon Recorder Helper Tool

    

## <a id="id_1" class="anchor_top_offset"/>Introduction

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Due to limitations in JavaScript and browsers' API, there are   some actions that cannot be done by Katalon Recorder alone. In   these cases, Katalon Recorder will send commands to a CLI tool   named Katalon Recorder Helper to finish the actions.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder Helper is an open source project (<a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-recorder-helper" target="_blank">https://github.com/katalon-studio/katalon-recorder-helper</a>).   It is actually a very lightweight Java server that listens for   commands from Katalon Recorder. It is built on top of the Spring   Boot framework.</p> 
    
  
    

## <a id="id_2" class="anchor_top_offset"/>Usage

    
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">Install Java Runtime Environment version 8.x on your     machine.</li>   <li className="li">Download the latest file "katalon-recorder-helper.jar" from the     releases page <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-recorder-helper/releases" target="_blank">https://github.com/katalon-studio/katalon-recorder-helper/releases</a>.</li>   <li className="li">     <p className="p">Run the jar file using the following command</p>     <pre className="pre codeblock"><code>java -jar katalon-recorder-helper.jar{"\n"}</code></pre>   </li> </ol> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Recorder Helper will listen for commands at port   18910.</p> 
    
  
    

## <a id="id_3" class="anchor_top_offset"/>Working with Katalon Recorder

    
          
      

### <a id="id_4" class="anchor_top_offset"/>Upload file

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For testing input elements with type="file" on Firefox, the   command "type | locator | filepath" only works when Katalon   Recorder Helper has started. It utilizes Java's Robot to trigger   key presses in order to manipulate the "File Upload"    dialog.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For Chrome, Katalon Recorder Helper is not required.</p> 
      
    

### <a id="id_5" class="anchor_top_offset"/>Executing OS commands

<p xmlns="http://www.w3.org/1999/xhtml" className="p">OS commands can be triggered using Katalon Recorder Helper.   Users can combine this function with user extensions (<a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-recorder-extension/get-your-job-done/extend-katalon-recorder/extension-scripts-for-custom-locator-builders-and-actions-in-katalon-recorder">Extension Scripts (extension.js) for Custom Locator Builders and Locators</a>) to extend   Katalon Recorder's capability.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, a call to the following URL</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>http://localhost:18910/execute?cmd=dir{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">will make the tool execute the "dir" command and return the   following response in JSON format</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>{"{"}{"\n"}{"  "}"command": "dir",{"\n"}{"  "}"output": [{"\n"}{"    "}" Volume in drive D is Data",{"\n"}{"    "}" Volume Serial Number is 1031-445A",{"\n"}{"    "}"",{"\n"}{"    "}" Directory of D:\\katalon-recorder-helper",{"\n"}{"    "}"",{"\n"}{"    "}"05/17/2018{"  "}12:55 PM{"    "}&lt;DIR&gt;{"          "}.",{"\n"}{"    "}"05/17/2018{"  "}12:55 PM{"    "}&lt;DIR&gt;{"          "}..",{"\n"}{"    "}"05/15/2018{"  "}09:17 AM{"               "}268 .gitignore",{"\n"}{"    "}"05/17/2018{"  "}01:14 PM{"    "}&lt;DIR&gt;{"          "}.idea",{"\n"}{"    "}"05/17/2018{"  "}11:58 AM{"             "}1,090 LICENSE",{"\n"}{"    "}"05/17/2018{"  "}12:47 PM{"             "}1,488 pom.xml",{"\n"}{"    "}"05/17/2018{"  "}12:26 PM{"               "}500 README",{"\n"}{"    "}"05/15/2018{"  "}04:17 PM{"    "}&lt;DIR&gt;{"          "}src",{"\n"}{"    "}"05/17/2018{"  "}12:55 PM{"    "}&lt;DIR&gt;{"          "}target",{"\n"}{"    "}"{"               "}4 File(s){"          "}3,346 bytes",{"\n"}{"    "}"{"               "}5 Dir(s){"  "}155,350,253,568 bytes free"{"\n"}{"  "}]{"\n"}{"}"}{"\n"}</code></pre> 
