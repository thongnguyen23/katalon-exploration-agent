---
hide_title: true
title: Real-time Monitoring and Reporting in Katalium Framework
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_katalium-framework-reports" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Real-time Monitoring and Reporting in Katalium Framework

    

## <a id="id_1" class="anchor_top_offset"/>TestNG Reports

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After execution, TestNG will generate a test-output folder at   the root of the project.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">target/surefire-reports</code> </p> 
    
  

## <a id="id_2" class="anchor_top_offset"/>For real-time monitoring and reporting using Katalon         Analytics

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Go to <code className="ph codeph">src</code> &gt; <code className="ph codeph">test</code> &gt;   <code className="ph codeph">kata-default.properties</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Set default values for parameters in the file   <code className="ph codeph">kata-default.properties</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, kataProjectId=2, the Project ID will be displayed   as <code className="ph codeph">https://analytics.katalon.com/team/1/project/2</code></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See real-time monitoring progress of the test execution:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-framework/docs/katalium-framework-reports/1-test-results.png")} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-framework/docs/katalium-framework-reports/2-test-results.png")} /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">With Katalium extension in Visual Studio Code, this will be       automatically setup.</p>   </li><li className="li">     <p className="p">With other IDEs, you need to set values for parameters in the       files <code className="ph codeph">&lt;user_home&gt;/.katalon/framework.properties</code>       in Katalium Framework.</p>     <p className="p">KATALON_API_KEY: Enter the API Key. You can generate new       API keys at <code className="ph codeph">https://analytics.katalon.com</code>. Go to <strong className="ph b">         <a className="xref j-external-link" href="https://analytics.katalon.com/user/profile" target="_blank">Profile</a>       </strong>       &gt; <strong className="ph b">Create API Key</strong> &gt; Input key name &gt; Click       <strong className="ph b">Create</strong>.</p>     <p className="p">KATALON_EMAIL: Enter your Katalon account. You can sign up for a       free account at <code className="ph codeph">https://www.katalon.com</code>.</p>     <p className="p">For example:</p>     <pre className="pre codeblock"><code>KATALON_API_KEY=8077730e-0e09-4b9d-a959-1a62b0a0d6f2{"\n"}KATALON_EMAIL=info@katalon.com{"\n"}</code></pre>   </li></ul> 
