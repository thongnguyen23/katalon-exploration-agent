---
hide_title: true
title: '[WebUI] Navigate to masked URL'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-1179" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Navigate to masked URL

<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">Katalon Studio version 9.1.0 onwards.</li></ul></div>

## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Navigate to a webpage with a masked URL. The URL will be masked with "*" in Console log, Log Viewer, and test reports. This keyword ensures privacy and confidentiality when sharing test results.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">navigateToMaskedUrl</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1">Parameter</th><th className="entry anchor_top_offset" id="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3">Required</th><th className="entry anchor_top_offset" id="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4 ">rawUrl</td><td className="entry" headers="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4 ">String</td><td className="entry" headers="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4 ">Yes</td><td className="entry" headers="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4 "><p className="p">URL of web page to navigate to.If <code className="ph codeph">rawUrl</code> doesn't contain protocol prefix, the the protocol will be <code className="ph codeph">http://</code>.</p><p className="p">Example:</p><ul className="ul"><li className="li">http://katalon.com</li><li className="li">https://www.google.com</li><li className="li">file:///D:Development/index.html;</li><li className="li">kms-technology.com =&gt; http://kms-technology.com</li></ul></td></tr><tr className><td className="entry" headers="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4 ">flowControl</td><td className="entry" headers="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4 ">FailureHandling</td><td className="entry" headers="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4 ">Optional</td><td className="entry" headers="concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__1 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__2 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__3 concept-1179__7c75ab19-2740-4d9c-9d21-b8b5726d85bb__entry__4 ">Specify <p className="p"><a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a></p> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## Example

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
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject

WebUI.comment('Story: Login to CURA system')

WebUI.comment('Given that the user has the valid login information')

WebUI.openBrowser('')

WebUI.navigateToMaskedUrl('http://demoaut.katalon.com')
WebUI.click(findTestObject('Page_CuraHomepage/btn_MakeAppointment'))

WebUI.closeBrowser()
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The URL <code className="ph codeph">http://demoaut.katalon.com</code> , which is input as raw text, will be masked:<img className="image" width={700} src={useBaseUrl("/23ea5840-8dbd-11ee-ab4f-0242c7a41fd4/KS_navigateToMaskedUrl_example.png")} alt="Masked URL in Log Viewer" /></p> 
