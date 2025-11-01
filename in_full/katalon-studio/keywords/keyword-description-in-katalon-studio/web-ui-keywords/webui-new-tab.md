---
hide_title: true
title: '[WebUI] New Tab'
---

# <a id="id_0-nw0verc0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] New Tab

<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Your Katalon Studio version must be <strong className="ph b">10.0.0+</strong>.</p></li></ul></div>

## <a id="id_0-nw0verc0__id_1" class="anchor_top_offset"/>Description  

              
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Create a new tab and focus on the new tab on the screen.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If multiple tabs are open, you can loop through the tabs visible to WebDriver and switch to the one which is not the original. If this step fails and <code className="ph codeph">takeScreenshot</code> is enabled, a screenshot will be taken.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">newTab</code></p> 
      
:::info notes
The `newTab` keyword is not supported when using Katalon Web Recorder with Firefox.
:::

## <a id="id_0-nw0verc0__id_2" class="anchor_top_offset"/>Parameters  

              
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4 ">rawUrl</td><td className="entry" headers="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4 ">String</td><td className="entry" headers="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4 ">Yes</td><td className="entry" headers="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4 ">The URL of the web page to be opened can be left empty or null. If rawUrl doesn't contain a protocol prefix, the protocol will be http://. For example:<ul className="ul"><li className="li"><p className="p">https://www.google.com</p></li><li className="li"><p className="p">file:///D:/Development/index.html</p></li><li className="li"><p className="p">kms-technology.com =&gt; http://kms-technology.com</p></li><li className="li"><p className="p">http://katalon.com/</p></li></ul></td></tr><tr className><td className="entry" headers="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4 ">flowControl</td><td className="entry" headers="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4 ">FailureHandling</td><td className="entry" headers="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4 ">Optional</td><td className="entry" headers="id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__1 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__2 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__3 id_0-nw0verc0__0192cb7e-af8b-4c15-96d0-797fdf360628__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to         determine whether the execution should be allowed to continue or         stop.</td></tr></tbody></table> 
      

## <a id="id_0-nw0verc0__id_3" class="anchor_top_offset"/>Example 

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

'Open a new tab'
WebUI.newTab('')

'Open a new tab and navigate to Google'
WebUI.newTab('https://www.google.com')
```            
