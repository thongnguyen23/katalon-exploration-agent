---
hide_title: true
title: '[WebUI] Check'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Check


## <a id="id_0__id_1" class="anchor_top_offset"/>Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Check a toggle button (a checkbox or a radio button).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">check</code></p> 

## <a id="id_0__id_2" class="anchor_top_offset"/>Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4 ">to</td><td className="entry" headers="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4 ">TestObject</td><td className="entry" headers="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4 ">Yes</td><td className="entry" headers="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4 ">Represents a web element.</td></tr><tr className><td className="entry" headers="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4 ">flowControl</td><td className="entry" headers="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4 ">Optional</td><td className="entry" headers="id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__1 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__2 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__3 id_0__5ba72266-5c2c-47ed-8199-7f9dbfd70ed9__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## <a id="id_0__id_3" class="anchor_top_offset"/>Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You want to check on the <span className="ph uicontrol">Medicaid</span> checkbox after navigating to the Make Appointment page:</p> 

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
WebUI.click(findTestObject('Page_CuraAppointment/btn_BookAppointment'))

'Check on 'Medicaid' checkbox'
WebUI.check(findTestObject('Page_CuraAppointment/chk_Medicaid'))

WebUI.closeBrowser()
```