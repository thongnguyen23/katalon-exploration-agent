---
hide_title: true
title: Develop a customized report plugin in Katalon Studio
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Develop a customized report plugin in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A sample custom keyword plugin to demonstrate how to generate a   customized report.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This plugin provides a test listener that automatically   generates a test suite report with a customized format as a text   file under <em className="ph i">Reports</em> folder.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>Relevant project structure

    
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>katalon-studio-sample-report-plugin{"\n"}├── Keywords{"\n"}│{"   "}├── sample.report{"\n"}│{"   "}│{"   "}├── SampleReportUtil.groovy{"\n"}│{"   "}│{"   "}├── TxtReportBuilder.groovy{"\n"}├── Test Listeners{"\n"}│{"   "}├── SampleReportTSListener.groovy{"\n"}</code></pre> 
          
  

## <a id="id_2" class="anchor_top_offset"/>How to build

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Open this project with <span className="ph">Katalon Studio</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Run the following command at the root folder:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>gradle katalonPluginPackage{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The plugin will be located at   <em className="ph i">build/libs/katalon-studio-sample-report-plugin.jar</em>   afterwards.</p> 
    

## <a id="id_3" class="anchor_top_offset"/>How to use

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Copy the above jar file and place it under <em className="ph i">Plugins</em>   folder of your Katalon project.</p> 
    
  
