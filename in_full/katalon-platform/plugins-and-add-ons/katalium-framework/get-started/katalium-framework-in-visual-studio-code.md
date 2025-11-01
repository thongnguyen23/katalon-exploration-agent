---
hide_title: true
title: Katalium Framework in Visual Studio Code
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_katalium-framework-get-started-vscode" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Katalium Framework in Visual Studio Code

    

## <a id="id_1" class="anchor_top_offset"/>Prerequisites

    
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Visual Studio Code.</li>   <li className="li">Java Development Kit 8.</li> </ul> 
    
  
    

## <a id="id_2" class="anchor_top_offset"/>Install Katalium Extension for Visual Studio Code

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Install Katalium Extension <a className="xref j-external-link" href="https://marketplace.visualstudio.com/items?itemName=katalon-llc.katalium" target="_blank">here</a>.</p> 
    
  
    

## <a id="id_3" class="anchor_top_offset"/>Activate

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Visual Studio Code, enter Katalon email and password to   activate.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-framework/docs/katalium-framework-get-started-vscode/activate.gif")} /><br /><br /> </p> 
    
  

## <a id="id_4" class="anchor_top_offset"/>Create project

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click <strong className="ph b">Create Project</strong> button to create a new   project.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <em className="ph i">Note: Clean your Workspace folder before creating a new     project.</em> </p> 

## <a id="id_5" class="anchor_top_offset"/>Start Katalium Server

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To start Katalium Server, click <strong className="ph b">Start Server</strong>   button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <em className="ph i">Note: You can view server information in Output tab of     Katalium. For example:</em> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-framework/docs/katalium-framework-get-started-vscode/before-start-server-vscode.png")} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After starting server, open browser in   <code className="ph codeph">http://localhost:4444/</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-framework/docs/katalium-framework-get-started-vscode/start-server-vscode.png")} /><br /><br /> </p> 
    

## <a id="id_6" class="anchor_top_offset"/>Run your first test in Visual Studio Code

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-framework/docs/katalium-framework-get-started-vscode/run-test-vscode.png")} /><br /><br /> </p> 
    
  

## <a id="id_7" class="anchor_top_offset"/>Run your first test in CLI

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To run the default test suite configured in <code className="ph codeph">pom.xml</code>   use <code className="ph codeph">mvn clean test</code>. Test suites can also be specified   using command arguments, e.g. <code className="ph codeph">mvn clean test     -Dsurefire.suiteXmlFiles=src/test/resources/testng-parallel.xml</code>.</p> 
