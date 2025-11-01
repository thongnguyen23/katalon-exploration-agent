---
hide_title: true
title: Writing Custom Script Formatter in Katalon Recorder
---

# <a id="id_writing-custom-script-formatter" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Writing Custom Script Formatter in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 

    

## <a id="id_1" class="anchor_top_offset"/>Introduction

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Starting from version 3.4.0, Katalon Recorder provides a plugin   platform for people to extend its capabilities.</p> 
    
  

## <a id="id_2" class="anchor_top_offset"/>List of Plugins

<p xmlns="http://www.w3.org/1999/xhtml" className="p">PHPUnit formatter for Katalon Recorder (<a className="xref j-external-link" href="https://bitbucket.org/inventis/phpunit-formatter-katalon-recorder/src/master/" target="_blank">Bitbucket</a>)   by Jan Esser. Selenide formatter for Katalon Recorder (<a className="xref j-external-link" href="https://chrome.google.com/webstore/detail/selenide-exporter-for-kat/mkbfcgpbkcaieiajhllpdocjfnfcbmlm" target="_blank">Chrome</a>)   by John Pratt.</p> 
    

## <a id="id_3" class="anchor_top_offset"/>Sample

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This is a sample plugin for Katalon Recorder <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-recorder-sample-plugin" target="_blank">https://github.com/katalon-studio/katalon-recorder-sample-plugin</a>.   This sample plugin adds plain text format, e.g.</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>open | https://katalon-test.s3.amazonaws.com/demo-aut/dist/html/form.html | {"\n"}click | id=first-name | {"\n"}type | id=first-name | Alex {"\n"}type | id=last-name | Smith{"\n"}</code></pre> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See the following demos for Chrome and Firefox.</p> 
    
  
