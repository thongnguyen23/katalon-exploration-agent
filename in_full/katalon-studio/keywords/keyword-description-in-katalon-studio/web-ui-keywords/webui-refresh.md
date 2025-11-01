---
hide_title: true
title: '[WebUI] Refresh'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Refresh


## <a id="id_0__id_1" class="anchor_top_offset"/>Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Simulate users clicking the Refresh button on their browser. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">refresh</code></p> 

## <a id="id_0__id_2" class="anchor_top_offset"/>Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__1 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__2 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__3 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__4 ">flowControl</td><td className="entry" headers="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__1 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__2 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__3 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__1 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__2 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__3 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__4 ">Optional</td><td className="entry" headers="id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__1 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__2 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__3 id_0__a6baa834-83d6-45e3-8ced-f0a7ac998bfd__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## <a id="id_0__id_3" class="anchor_top_offset"/>Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You want to refresh the current web page:</p> 

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

'Open browser'
WebUI.openBrowser('')

'Navigate to demo AUT site'
WebUI.navigateToUrl('http://demoaut.katalon.com/')

'Refresh the current web page'
WebUI.refresh()

'Close browser'
WebUI.closeBrowser()
```