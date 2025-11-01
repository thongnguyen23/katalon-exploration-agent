---
hide_title: true
title: Katalium Framework in other IDEs
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_katalium-framework-get-started-other-ides" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Katalium Framework in other IDEs

    

## <a id="id_1" class="anchor_top_offset"/>Prerequisites

    
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Java Development Kit 8.</li> </ul> 
    
  
    

## <a id="id_2" class="anchor_top_offset"/>Start Katalium Server

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Please refer to <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalium-server/get-started-with-katalium-server">this     guide</a> to learn how to start Katalium Server.</p> 
    
  
    

## <a id="id_3" class="anchor_top_offset"/>Run your first test in IDE

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Refer to this guide to learn how to <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalium-framework/create-a-test-case-in-katalium-framework">create     a test case</a> or <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalium-framework/create-a-test-suite-in-katalium-framework">test     suite</a>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example of a test case run in IntelliJ IDEA:</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-framework/docs/katalium-framework-get-started-other-ides/run-test-ide.png")} /><br /><br /> </p> 
    
  

## <a id="id_4" class="anchor_top_offset"/>Run your first test in CLI

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To run the default test suite configured in <code className="ph codeph">pom.xml</code>   use <code className="ph codeph">mvn clean test</code>. Test suites can also be specified   using command arguments, e.g. <code className="ph codeph">mvn clean test     -Dsurefire.suiteXmlFiles=src/test/resources/testng-parallel.xml</code>.</p> 
