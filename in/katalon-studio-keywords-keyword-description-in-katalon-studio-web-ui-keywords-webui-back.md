---
hide_title: true
title: '[WebUI] Back'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Back


## <a id="id_0__id_1" class="anchor_top_offset"/>Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Simulate users clicking the Back button on their browser.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">back</code></p> 

## <a id="id_0__id_2" class="anchor_top_offset"/>Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__1 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__2 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__3 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__4 ">flowControl</td><td className="entry" headers="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__1 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__2 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__3 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__1 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__2 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__3 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__4 ">Optional</td><td className="entry" headers="id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__1 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__2 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__3 id_0__9a241b44-efa0-4a2f-82fa-f9b2d14196a0__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## <a id="id_0__id_3" class="anchor_top_offset"/>Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You want to go back to the previous page after a successful navigation:</p> 

```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

'Open browser and navigate to demo AUT site'
WebUI.openBrowser('http://demoaut.katalon.com/')

'Click on 'Make Appointment' button'
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))

'Back to previous page after navigating to 'Make Appointment' page'
WebUI.back()

'Close browser'
WebUI.closeBrowser()
```