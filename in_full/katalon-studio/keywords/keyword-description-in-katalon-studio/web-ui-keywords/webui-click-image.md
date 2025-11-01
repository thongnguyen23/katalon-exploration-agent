---
hide_title: true
title: '[WebUI] Click Image'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Click Image

<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Known limitation:</span> <p className="p">The <code className="ph codeph">clickImage</code> keyword may not function as expected in Safari due to browser-specific limitations in handling image objects. We recommend using other browsers like Chrome or Firefox for this image-based operation.</p></div>

## <a id="id_0__id_1" class="anchor_top_offset"/>Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on an image on the web page.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">clickImage</code><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">The <code className="ph codeph">clickImage</code> keyword is not supported in headless browser mode.</p></li></ul></div></div>

## <a id="id_0__id_2" class="anchor_top_offset"/>Parameters 

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__dc710f06-0d76-4969-bb70-7157e15ad099"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4 ">to</td><td className="entry" headers="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4 ">TestObject</td><td className="entry" headers="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4 ">Yes</td><td className="entry" headers="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4 ">Represents an image.</td></tr><tr className><td className="entry" headers="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4 ">flowControl</td><td className="entry" headers="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4 ">Optional</td><td className="entry" headers="id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__1 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__2 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__3 id_0__dc710f06-0d76-4969-bb70-7157e15ad099__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## <a id="id_0__id_3" class="anchor_top_offset"/>Example 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You want to click on the <code className="ph codeph">img_Logo</code> image:</p> 

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

'Open browser and navigate to a site that contains the image to click on'
WebUI.openBrowser(GlobalVariable.G_SiteURL)

'Click on the image'
WebUI.clickImage(findTestObject('img_Logo'))

'Close browser'
WebUI.closeBrowser()
```