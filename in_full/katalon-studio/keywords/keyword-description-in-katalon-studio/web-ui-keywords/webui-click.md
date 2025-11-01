---
hide_title: true
title: '[WebUI] Click'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# [WebUI] Click

## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on the given element. If the target element is behind a loading overlay, Katalon Studio repeatedly tries clicking the element for a period of time as configured in <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Execution</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Default wait for element timeout</span></span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">click</code></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/wait-for-element-timeout/KS-OVERLAY-Default-timeout-settings.png")} width={700} alt="Default wait for element timeout settings" /><br /><br /></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4 ">to</td><td className="entry" headers="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4 ">TestObject</td><td className="entry" headers="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4 ">Yes</td><td className="entry" headers="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4 ">Represents a web element.</td></tr><tr className><td className="entry" headers="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4 ">flowControl</td><td className="entry" headers="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4 ">Optional</td><td className="entry" headers="id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__1 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__2 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__3 id_0__113e9f03-ca86-4064-be94-53c9f22f66d1__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, we want to click on the <span className="ph uicontrol">Make Appointment</span> button. By default, the Default wait for element timeout setting is for 30 seconds. If the <span className="ph uicontrol">Make Appointment</span> button is behind a loading overlay, Katalon Studio will try clicking the button for 30 seconds maximum:</p> 

```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
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

'Open browser and navigate to demo AUT site.'
WebUI.openBrowser(GlobalVariable.G_SiteURL)

'Click on 'Book Appointment' button'
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))

'Close browser'
WebUI.closeBrowser()
```

<div xmlns="http://www.w3.org/1999/xhtml" className="p">Alternatively, you can try <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-execute-javascript">[WebUI] Execute JavaScript</a> to click the element, as shown in the example code below: </div>

```jsx
WebElement element = WebUiCommonHelper.findWebElement(findTestObject('your/object'),30)
WebUI.executeJavaScript("arguments[0].click()", Arrays.asList(element))
```