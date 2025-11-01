---
hide_title: true
title: Solving Wait-time issue with Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Solving Wait-time issue with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Automation execution usually does not carry out exactly as   scripted due to many factors involved during execution such as   network stability, internet bandwidth, the performance of the AUT,   and the performance of the executing computer. This article will   guide users through leveraging delayed time to handle such   situations.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">What is Wait?</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Using delayed time is a common practice in test automation   scripts to create a pause in-between automation steps as you wait   for web elements to load or for the AUT to respond.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here are some examples of test failure due to insufficient   waiting time:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <strong className="ph b">False Fail:</strong> One of the most common failures is     when a script fails due to waiting on the application. It is often     caused by network latency, delayed database requests, or simply     because the system needs more time to process and respond to the     request.</li><li className="li">     <strong className="ph b">Targeted element not present on the page:</strong> This     kind of failure occurs when waiting for elements to be displayed or     rendered in the browser. The application may be up and running but     certain elements may not be loaded, thus causing test scripts to     fail.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">How to address those failures related to     Wait?</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon provides keywords dedicated to delay explicitly. You can   use the following options to address the situation:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">       <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/webui-wait-for-page-load.html" target="_blank">         <strong className="ph b">Wait           For Page Load</strong>       </a>       <strong className="ph b">–</strong> This logic will       wait for a page to completely load before running a step in your       script.</p>   </li><li className="li">     <p className="p">       <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/webui-wait-for-element-present.html" target="_blank">         <strong className="ph b">Wait           For Element Present</strong>       </a>       <strong className="ph b">–</strong> It       happens sometimes that web elements take longer time to appear on       the page. This keyword pauses execution until the targeted element       appears on the page. Once the element appears, the test continues       to execute the next action.</p>   </li><li className="li">     <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/variable-types.html" target="_blank">       <strong className="ph b">Global         variable</strong>     </a>     <strong className="ph b">–</strong> This variable has     the global scope, meaning that it is visible throughout the     program. Thus, you can use this variable in your test scripts     according to the response time of your web application. You may     consider defining 3 kinds of global variable in your test scripts,     for short, medium, and long waits.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example: The script below shows the usage of a global   variable and the use of Katalon Studio built-in keyword <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/mobile-wait-for-element-present.html" target="_blank">     <strong className="ph b">Wait       For Element Present</strong>   </a> to deliberately wait for a   specific test element.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/solving_common_issue_wait_time/Wait-For-Element-Present.png")} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Figure 1: Katalon Studio test script</strong> </p> 

```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint</p>
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import internal.GlobalVariable as GlobalVariable
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS

'Open browser and navigate to Katalon site'
WebUI.openBrowser("https://katalon.com")

'Wait for Katalon Studio page to load with wait used as Global Variable'
WebUI.waitForPageLoad(GlobalVariable.G_Timeout_Small)
 
'Click on 'Login'  button to navigate to Login page'
WebUI.click(findTestObject('Page_KatalonHomepage/btn_Login'))
 
'Input username'
WebUI.setText(findTestObject('Page_Login/txt_UserName'), Username)
 
'Input password'
WebUI.setText(findTestObject('Page_Login/txt_Password'), Password)
 
'Click on 'Login'  button to login'
WebUI.click(findTestObject('Page_KatalonHomepage/btn_Submit'))
 
'Wait for failed message to be present'
WebUI.waitForElementPresent(findTestObject('Page_KataloLogin/div_LoginMessage'), GlobalVariable.G_Timeout_Small)
 
WebUI.closeBrowser()
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">When to use Wait Commands</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Quite often test execution get failed due to the exceptions such   as '<strong className="ph b">NoSuchElementException</strong>',   '<strong className="ph b">ElementNotFoundException</strong>',   '<strong className="ph b">ElementNotVisibleException</strong>'. In order to handle   these exceptions, conditional Synchronization has to be   implemented. Katalon Studio supports many built in "<strong className="ph b">Wait     for….</strong>" keywords to deal with such exceptions. For   example:</p> 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id__82341021-0c60-40c3-afc1-89d66a918687"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1">Keyword</th><th className="entry anchor_top_offset" id="id__82341021-0c60-40c3-afc1-89d66a918687__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1 id__82341021-0c60-40c3-afc1-89d66a918687__entry__2 ">         <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-wait-for-element-present">Wait           For Element Present</a>       </td><td className="entry" headers="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1 id__82341021-0c60-40c3-afc1-89d66a918687__entry__2 ">Wait for the given element to present (appear) within the given         time in seconds.</td></tr><tr className><td className="entry" headers="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1 id__82341021-0c60-40c3-afc1-89d66a918687__entry__2 ">         <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-wait-for-element-visible">Wait           For Element Visible</a>       </td><td className="entry" headers="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1 id__82341021-0c60-40c3-afc1-89d66a918687__entry__2 ">Wait until the given web element is visible within         timeout.</td></tr><tr className><td className="entry" headers="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1 id__82341021-0c60-40c3-afc1-89d66a918687__entry__2 ">         <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-wait-for-alert">Wait For           Alert</a>       </td><td className="entry" headers="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1 id__82341021-0c60-40c3-afc1-89d66a918687__entry__2 ">Wait for a browser's alert to present.</td></tr><tr className><td className="entry" headers="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1 id__82341021-0c60-40c3-afc1-89d66a918687__entry__2 ">         <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-wait-for-element-clickable">Wait for           Element Clickable</a>       </td><td className="entry" headers="id__82341021-0c60-40c3-afc1-89d66a918687__entry__1 id__82341021-0c60-40c3-afc1-89d66a918687__entry__2 ">Wait for the given element to be clickable within the given         time in seconds.</td></tr></tbody></table> 
