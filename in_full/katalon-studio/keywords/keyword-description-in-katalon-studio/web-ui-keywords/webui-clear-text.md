---
hide_title: true
title: '[WebUI] Clear Text'
---

# <a id="concept-6727" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Clear Text


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Clears all text of the test object using WebUI.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">clearText</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1">Parameter</th><th className="entry anchor_top_offset" id="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3">Required</th><th className="entry anchor_top_offset" id="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4 ">to</td><td className="entry" headers="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4 ">TestObject</td><td className="entry" headers="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4 ">Yes</td><td className="entry" headers="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4 ">Represents a web element.</td></tr><tr className><td className="entry" headers="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4 ">flowControl</td><td className="entry" headers="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4 ">FailureHandling</td><td className="entry" headers="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4 ">Optional</td><td className="entry" headers="concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__1 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__2 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__3 concept-6727__0dc0cdb7-4507-45e7-a8db-b6f773efad37__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## Returns

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph uicontrol">true</span> if text of object is clear. Otherwise, <span className="ph uicontrol">false</span>.</p> 

## Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You want to clear text in the login fields on the CURA Healthcare Service login page:</p> 

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

'Open browser and navigate to demo AUT site'
WebUI.openBrowser('http://demoaut.katalon.com')

'Click on 'Make Appointment' button'
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))

'Fill in login information'
WebUI.setText(findTestObject('Page_Login/txt_UserName'), Username)

WebUI.setText(findTestObject('Page_Login/txt_Password'), Password)

'Clear text in login fields'
WebUI.clearText(findTestObject('Page_Login/txt_UserName'))

WebUI.clearText(findTestObject('Page_Login/txt_Password'))

'Close browser'
WebUI.closeBrowser()
```