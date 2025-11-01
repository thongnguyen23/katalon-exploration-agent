---
hide_title: true
title: 'Example plugin: Build Katalon Studio TestRail Integration plugin'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Example plugin: Build Katalon Studio TestRail Integration plugin

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This document  shows you the way to implement Katalon   Studio TestRail integration plugin. All functions are   implemented using <em className="ph i">extension point</em>, which are declared in   <code className="ph codeph">plugin.xml</code>. You can see plugin’s activities by   selecting the tab <em className="ph i">Event Log</em> (next to   <em className="ph i">Console</em>): </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <a className="xref j-external-link" href="https://store.katalon.com/product/13/TestRail-Integration" target="_blank">TestRail Integration</a> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code is made available here on our GitHub repository for reference:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-testrail-plugin" target="_blank">Katalon Studio TestRail plugin</a> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This document is not about how to use the plugin.   Visit <a className="xref" href="/katalon-studio/integrations/test-management/configure-testrail-integration-in-katalon-studio">TestRail     integration document</a> if you need help.</p> 

## Setting page in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/1_connect.png")} /><br /><br /> </p> 

### Add an icon to the toolbar      

<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;extension{"\n"}{"        "}point="com.katalon.platform.extensions"&gt;{"\n"}{"    "}&lt;point{"\n"}{"            "}id="com.katalon.plugin.testrail.TestRailToolItemDescription"{"\n"}{"            "}extensionPointId="com.katalon.platform.api.extension.newToolItem"{"\n"}{"            "}implementationClass="com.katalon.plugin.testrail.TestRailToolItemDescription"&gt;{"\n"}{"    "}&lt;/point&gt;{"\n"}&lt;/extension&gt;{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For implementation, see class   <code className="ph codeph">com.katalon.plugin.testrail.TestRailToolItemDescription</code>.</p> 

### Add a setting page      

<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;extension{"\n"}{"      "}point="com.katalon.platform.extensions"&gt;{"\n"}{"  "}&lt;point{"\n"}{"        "}id="com.katalon.plugin.testrail.TestRailPluginPreferencePage"{"\n"}{"        "}extensionPointId="com.katalon.platform.api.extension.pluginPreferencePage"{"\n"}{"        "}implementationClass="com.katalon.plugin.testrail.TestRailPluginPreferencePage"&gt;{"\n"}{"  "}&lt;/point&gt;{"\n"}&lt;/extension&gt;{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For implementation, see classes   <code className="ph codeph">com.katalon.plugin.testrail.TestRailPluginPreferencePage</code>   and   <code className="ph codeph">com.katalon.plugin.testrail.TestRailPreferencePage</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Settings are saved per project.</p> 

## Link Katalon Studio Test Cases with TestRail  Test Cases    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/2_mapping.png")} /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;extension{"\n"}{"        "}point="com.katalon.platform.extensions"&gt;{"\n"}{"    "}&lt;point{"\n"}{"            "}id="com.katalon.plugin.testrail.TestRailTestCaseIntegrationPage"{"\n"}{"            "}extensionPointId="com.katalon.platform.api.extension.testCaseIntegrationViewDescription"{"\n"}{"            "}implementationClass="com.katalon.plugin.testrail.TestRailTestCaseIntegrationViewDescription"&gt;{"\n"}{"    "}&lt;/point&gt;{"\n"}&lt;/extension&gt;{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For implementation, see classes   <code className="ph codeph">com.katalon.plugin.testrail.TestRailTestCaseIntegrationViewDescription</code>   and   <code className="ph codeph">com.katalon.plugin.testrail.TestRailTestCaseIntegrationView</code>.</p> 

## Execute Test Cases selectively based on TestRail settings    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/4_querying.png")} /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;extension{"\n"}{"        "}point="com.katalon.platform.extensions"&gt;{"\n"}{"    "}&lt;point{"\n"}{"            "}id="com.katalon.plugin.dynamic_execution.TestRailFilteringTestSuiteImpl"{"\n"}{"            "}extensionPointId="com.katalon.platform.api.extension.dynamicQueryingTestSuiteDescription"{"\n"}{"            "}implementationClass="com.katalon.plugin.testrail.TestRailQueryingTestSuite"&gt;{"\n"}{"    "}&lt;/point&gt;{"\n"}&lt;/extension&gt;{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For implementation, see class   <code className="ph codeph">com.katalon.plugin.testrail.TestRailQueryingTestSuite</code>.</p> 

## Sending result to TestRail    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/3.1_sending.png")} /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;extension{"\n"}{"        "}point="com.katalon.platform.extensions"&gt;{"\n"}{"    "}&lt;point{"\n"}{"            "}id="com.katalon.plugin.testrail.TestRailEventListenerInitializer"{"\n"}{"            "}extensionPointId="com.katalon.platform.api.extension.eventListener"{"\n"}{"            "}implementationClass="com.katalon.plugin.testrail.TestRailEventListenerInitializer"&gt;{"\n"}{"    "}&lt;/point&gt;{"\n"}&lt;/extension&gt;{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For implementation, see class   <code className="ph codeph">com.katalon.plugin.testrail.TestRailEventListenerInitializer</code>.</p> 

## TestRail SDK    

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   You can also refer to TestRail document: <a className="xref j-external-link" href="http://docs.gurock.com/testrail-api2/bindings-java" target="_blank">Bindings Java.</a></p> 
